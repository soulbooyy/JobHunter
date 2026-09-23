"""Forward schema preservation and actual SQLite relational boundaries."""

import sqlite3
from pathlib import Path
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.application.candidate.preferences import Preferences
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.application.materials.service import Materials
from jobhunter.domain.derived_work.models import RenderRequest
from jobhunter.domain.manual_application_entries.models import CreateEntry
from jobhunter.domain.preferences.models import SavePreferences
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.invocation import TABLES
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials import (
    MaterialsRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault
from jobhunter.infrastructure.rendering.catalog import catalog
from sqlalchemy import create_engine


def historical_four(directory: Path) -> None:
    engine = create_engine(
        "sqlite://",
        creator=lambda: sqlite3.connect(directory / "jobhunter.sqlite3", isolation_level=None),
    )
    try:
        with engine.connect() as conn:
            conn.exec_driver_sql("PRAGMA foreign_keys=ON")
            conn.exec_driver_sql("BEGIN IMMEDIATE")
            config = Config(str(Path(__file__).resolve().parents[3] / "alembic.ini"))
            config.attributes["connection"] = conn
            config.attributes["fault"] = no_fault
            command.upgrade(config, "a41d7e90c263")
            conn.commit()
    finally:
        engine.dispose()


def snapshot(store: Store) -> dict[str, list[tuple[object, ...]]]:
    with store.engine.connect() as conn:
        names = (
            conn.exec_driver_sql(
                "SELECT name FROM sqlite_master WHERE type='table' AND name!='alembic_version'"
            )
            .scalars()
            .all()
        )
        return {
            str(name): [tuple(row) for row in conn.exec_driver_sql(f"SELECT * FROM {name}").all()]
            for name in names
        }


def test_schema_four_forward_migration_preserves_every_existing_row(tmp_path: Path) -> None:
    historical_four(tmp_path)
    with Store.open(tmp_path, migration=True) as store:
        assert store.recognize() == 4
        Entries(store).create(
            CreateEntry(
                request_id=str(uuid4()),
                company_name="Exact",
                role_title="R",
                application_url="https://example.test",
            )
        )
        candidate = CandidateAuthority(store)
        resume = candidate.command(
            "RESUME_CREATE",
            {
                "request_id": str(uuid4()),
                "resume_name": "Exact source",
                "profile_version_id": candidate.pair("profile")["profile_version"][
                    "profile_version_id"
                ],
                "header_presentation": {"optional_items": []},
                "sections": [],
                "document_presentation": {
                    "font_family": "HEITI",
                    "font_size_pt": 12,
                    "line_spacing_pt": 14,
                    "theme_color": "#000000",
                },
            },
        )
        configuration = catalog()[0]
        store.run(lambda conn: MaterialsRepository(conn).register(configuration), write=True)
        materials = Materials(store, capability=lambda _: True)
        render_command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=resume["resume_version"]["resume_version_id"],
            render_configuration_id=configuration.render_configuration_id,
        )
        render_result = materials.request(render_command)
        preference_command = SavePreferences.model_validate(
            {
                "request_id": str(uuid4()),
                "revision": None,
                "configuration": {
                    "target_job_keywords": ["Exact"],
                    "accepted_cities": {"mode": "UNLIMITED"},
                    "minimum_salary": {"mode": "UNLIMITED"},
                    "recruitment_types": {"mode": "UNLIMITED"},
                    "excluded_companies": {"mode": "UNLIMITED"},
                    "max_required_education": {"mode": "UNLIMITED"},
                },
            }
        )
        preference_result = Preferences(store).save(preference_command)
        before = snapshot(store)
        assert store.migrate() == "MIGRATED"
        after = snapshot(store)
        assert {k: after[k] for k in before} == before
        assert all(after[name] == [] for name, _ in TABLES)
        assert store.recognize() == 5
        assert store.migrate() == "UNCHANGED"
        assert materials.request(render_command) == render_result
        assert Preferences(store).save(preference_command) == preference_result
    with Store.open(tmp_path) as store:
        assert snapshot(store) == after


@pytest.mark.parametrize(
    "stage", ["migration_" + name for name, _ in TABLES] + ["migration_invocation_version"]
)
def test_interrupted_forward_migration_retains_complete_schema_four(
    tmp_path: Path, stage: str
) -> None:
    historical_four(tmp_path)
    with pytest.raises(Failure, match="SCHEMA_UNSUPPORTED"):
        Store.open(tmp_path)

    def fail(point: str) -> None:
        if point == stage:
            raise OSError("private SQL payload")

    with Store.open(tmp_path, migration=True, fault=fail) as store:
        before = snapshot(store)
        with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
            store.migrate()
        assert store.recognize() == 4
        assert snapshot(store) == before
        store.fault = no_fault
        assert store.migrate() == "MIGRATED"


def test_runtime_reference_integrity_is_enforced_by_sqlite(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        with pytest.raises(Failure, match="OUTCOME_UNKNOWN"):
            store.run(
                lambda c: c.exec_driver_sql(
                    "INSERT INTO invocation_responses VALUES (?,?,?,?,?)",
                    (str(uuid4()), "controlled.response.v1", b"{}", "0" * 64, 2),
                ),
                write=True,
            )
        assert (
            store.run(
                lambda c: c.exec_driver_sql("SELECT count(*) FROM invocation_responses").scalar()
            )
            == 0
        )
