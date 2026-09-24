"""Add Entry-scoped immutable portrait plans without another development reset."""

from collections.abc import Callable
from typing import Any, cast
from uuid import uuid4

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v3 import (
    PORTRAIT_BUILD_DDL,
    PORTRAIT_DERIVATION_DDL,
    ddl,
)
from sqlalchemy.engine import Connection

revision = "8c92f0d4ae31"
down_revision = "f4b31d8c2a70"
branch_labels = None
depends_on = None


def insert(conn: Connection, table: str, row: dict[str, Any]) -> None:
    conn.exec_driver_sql(
        f"INSERT INTO {table} ({','.join(row)}) VALUES ({','.join('?' for _ in row)})",
        tuple(row.values()),
    )


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    conn = op.get_bind()
    builds = [dict(row) for row in conn.exec_driver_sql("SELECT * FROM portrait_builds").mappings()]
    state = dict(
        conn.exec_driver_sql("SELECT * FROM current_portrait_state WHERE singleton_key=1")
        .mappings()
        .one()
    )
    receipts = [
        dict(row)
        for row in conn.exec_driver_sql("SELECT * FROM candidate_command_receipts").mappings()
    ]

    op.execute("PRAGMA defer_foreign_keys=ON")
    for table in ("candidate_command_receipts", "current_portrait_state", "portrait_builds"):
        op.execute(f"DROP TABLE {table}")
        fault("migration_entry_incremental_drop_" + table)

    op.execute(PORTRAIT_BUILD_DDL)
    fault("migration_entry_incremental_portrait_builds")
    for row in builds:
        status = "OBSOLETE" if row["status"] == "SUCCEEDED" else row["status"]
        insert(
            conn,
            "portrait_builds",
            {
                **row,
                "trigger_mode": "AUTOMATIC",
                "status": status,
                "failure_code": row["failure_code"] if status == "FAILED" else None,
                "configuration_key": None,
                "baseline_portrait_id": None,
                "reattachment_portrait_id": None,
                "plan": None,
                "run_id": None,
                "result_portrait_id": None,
                "disposition": None,
            },
        )

    if state["status"] == "READY":
        prior = next(row for row in builds if row["build_id"] == state["build_id"])
        replacement_id = str(uuid4())
        insert(
            conn,
            "portrait_builds",
            {
                "build_id": replacement_id,
                "source_resume_version_id": state["source_resume_version_id"],
                "selection_revision": prior["selection_revision"],
                "extraction_key": prior["extraction_key"],
                "trigger_mode": "AUTOMATIC",
                "status": "QUEUED",
                "failure_code": None,
                "created_at": prior["created_at"],
                "configuration_key": None,
                "baseline_portrait_id": None,
                "reattachment_portrait_id": None,
                "plan": None,
                "run_id": None,
                "result_portrait_id": None,
                "disposition": None,
            },
        )
        state.update(
            status="QUEUED",
            build_id=replacement_id,
            portrait_id=None,
            failure_code=None,
        )

    op.execute(ddl("current_portrait_state"))
    fault("migration_entry_incremental_current_portrait_state")
    insert(conn, "current_portrait_state", state)
    op.execute(ddl("candidate_command_receipts"))
    fault("migration_entry_incremental_candidate_command_receipts")
    for row in receipts:
        insert(conn, "candidate_command_receipts", row)
    op.execute(PORTRAIT_DERIVATION_DDL)
    fault("migration_entry_incremental_portrait_derivations")
    op.execute("PRAGMA user_version=7")
    fault("migration_entry_incremental_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
