"""Schema-7 Entry-scoped portrait planning and successful-derivation order."""

# ruff: noqa: E501 -- exact SQLite DDL is compared during storage recognition.

from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v2 import (
    TABLES as SCHEMA_SIX_TABLES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v2 import fk
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials import optional_identity
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import identity
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import timestamp_column

ALEMBIC_REVISION = "8c92f0d4ae31"
SCHEMA_VERSION = 7

PORTRAIT_BUILD_DDL = f"""CREATE TABLE portrait_builds (
{identity("build_id", True)}, {identity("source_resume_version_id")},
selection_revision INTEGER NOT NULL CHECK(typeof(selection_revision)='integer' AND selection_revision BETWEEN 1 AND 9007199254740991),
extraction_key TEXT NOT NULL,
trigger_mode TEXT NOT NULL CHECK(trigger_mode IN ('AUTOMATIC','FULL')),
status TEXT NOT NULL CHECK(status IN ('QUEUED','RUNNING','SUCCEEDED','FAILED','OBSOLETE')),
failure_code TEXT, {timestamp_column("created_at")},
configuration_key TEXT CHECK(configuration_key IS NULL OR (length(configuration_key) BETWEEN 1 AND 128)),
{optional_identity("baseline_portrait_id")}, {optional_identity("reattachment_portrait_id")},
plan TEXT CHECK(plan IS NULL OR (typeof(plan)='text' AND json_valid(plan) AND json_type(plan)='object')),
{optional_identity("run_id")}, {optional_identity("result_portrait_id")},
disposition TEXT CHECK(disposition IN ('NEW_PAIR','REATTACHED')),
CHECK((status='FAILED')=(failure_code IS NOT NULL)),
CHECK((configuration_key IS NULL)=(plan IS NULL)),
CHECK(trigger_mode='AUTOMATIC' OR (baseline_portrait_id IS NULL AND reattachment_portrait_id IS NULL)),
CHECK(reattachment_portrait_id IS NULL OR reattachment_portrait_id=baseline_portrait_id),
CHECK((status='SUCCEEDED')=(result_portrait_id IS NOT NULL AND disposition IS NOT NULL)),
CHECK(status='SUCCEEDED' OR (result_portrait_id IS NULL AND disposition IS NULL)),
{fk("source_resume_version_id", "resume_versions", "resume_version_id")},
{fk("source_resume_version_id", "candidate_evidence_projections", "resume_version_id")},
{fk("baseline_portrait_id", "portraits", "portrait_id")},
{fk("reattachment_portrait_id", "portraits", "portrait_id")},
{fk("run_id", "agent_runs", "run_id")},
{fk("result_portrait_id", "portraits", "portrait_id")})"""

PORTRAIT_DERIVATION_DDL = f"""CREATE TABLE portrait_derivations (
{identity("portrait_id", True)}, {identity("resume_id")}, {identity("resume_version_id")},
extraction_key TEXT NOT NULL, configuration_key TEXT NOT NULL CHECK(length(configuration_key) BETWEEN 1 AND 128),
derivation_order INTEGER NOT NULL UNIQUE CHECK(typeof(derivation_order)='integer' AND derivation_order BETWEEN 1 AND 9007199254740991),
{timestamp_column("created_at")},
{fk("portrait_id", "portraits", "portrait_id")},
{fk("resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")})"""

TABLES: tuple[tuple[str, str], ...] = tuple(
    (name, PORTRAIT_BUILD_DDL if name == "portrait_builds" else ddl)
    for name, ddl in SCHEMA_SIX_TABLES
    if name != "portrait_derivations"
) + (("portrait_derivations", PORTRAIT_DERIVATION_DDL),)


def ddl(name: str) -> str:
    return dict(TABLES)[name]
