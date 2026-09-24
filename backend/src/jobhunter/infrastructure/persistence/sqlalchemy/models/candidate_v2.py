"""Schema-6 independent Resume authority and deterministic portrait preparation."""

# ruff: noqa: E501 -- exact versioned SQLite DDL is kept visually comparable.

from collections.abc import Callable

from sqlalchemy.engine import Connection

from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import identity
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import timestamp_column

ALEMBIC_REVISION = "f4b31d8c2a70"
SCHEMA_VERSION = 6
KINDS = "'EDUCATION','WORK_EXPERIENCE','PROJECT','SKILL','AWARD','CERTIFICATION'"


def fk(columns: str, table: str, target: str) -> str:
    return f"FOREIGN KEY({columns}) REFERENCES {table}({target}) DEFERRABLE INITIALLY DEFERRED"


def json_column(name: str, kind: str = "object") -> str:
    return (
        f"{name} TEXT NOT NULL CHECK(typeof({name})='text' AND json_valid({name}) "
        f"AND json_type({name})='{kind}')"
    )


TABLES: tuple[tuple[str, str], ...] = (
    (
        "resumes",
        f"""CREATE TABLE resumes (
{identity("resume_id", True)}, resume_name TEXT NOT NULL,
status TEXT NOT NULL CHECK(status IN ('ACTIVE','REMOVED')),
{identity("current_resume_version_id")},
revision INTEGER NOT NULL CHECK(typeof(revision)='integer' AND revision BETWEEN 1 AND 9007199254740991),
{timestamp_column("created_at")}, {timestamp_column("updated_at")},
UNIQUE(resume_id,current_resume_version_id),
{fk("current_resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")})""",
    ),
    (
        "resume_versions",
        f"""CREATE TABLE resume_versions (
{identity("resume_version_id", True)}, {identity("resume_id")},
schema_version INTEGER NOT NULL CHECK(typeof(schema_version)='integer' AND schema_version=2),
{json_column("contacts")}, {json_column("header_presentation")},
{json_column("document_presentation")}, {timestamp_column("created_at")},
UNIQUE(resume_version_id,resume_id),
{fk("resume_id", "resumes", "resume_id")})""",
    ),
    (
        "resume_entry_owners",
        f"""CREATE TABLE resume_entry_owners (
{identity("entry_id", True)}, {identity("resume_id")}, UNIQUE(entry_id,resume_id),
{fk("resume_id", "resumes", "resume_id")})""",
    ),
    (
        "resume_block_owners",
        f"""CREATE TABLE resume_block_owners (
{identity("block_id", True)}, {identity("resume_id")}, UNIQUE(block_id,resume_id),
{fk("resume_id", "resumes", "resume_id")})""",
    ),
    (
        "resume_sections",
        f"""CREATE TABLE resume_sections (
{identity("resume_version_id")}, position INTEGER NOT NULL CHECK(typeof(position)='integer' AND position>=0),
kind TEXT NOT NULL CHECK(kind IN ({KINDS})),
PRIMARY KEY(resume_version_id,position), UNIQUE(resume_version_id,kind),
{fk("resume_version_id", "resume_versions", "resume_version_id")})""",
    ),
    (
        "resume_entries",
        f"""CREATE TABLE resume_entries (
{identity("resume_version_id")}, {identity("resume_id")},
section_position INTEGER NOT NULL CHECK(typeof(section_position)='integer' AND section_position>=0),
position INTEGER NOT NULL CHECK(typeof(position)='integer' AND position>=0),
kind TEXT NOT NULL CHECK(kind IN ({KINDS})), {identity("entry_id")},
{json_column("fields")}, {json_column("content", "array")},
PRIMARY KEY(resume_version_id,section_position,position),
UNIQUE(resume_version_id,entry_id),
{fk("resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")},
{fk("resume_version_id,section_position", "resume_sections", "resume_version_id,position")},
{fk("entry_id,resume_id", "resume_entry_owners", "entry_id,resume_id")})""",
    ),
    (
        "resume_blocks",
        f"""CREATE TABLE resume_blocks (
{identity("resume_version_id")}, {identity("resume_id")}, {identity("entry_id")},
position INTEGER NOT NULL CHECK(typeof(position)='integer' AND position>=0), {identity("block_id")},
PRIMARY KEY(resume_version_id,entry_id,position), UNIQUE(resume_version_id,block_id),
{fk("resume_version_id,entry_id", "resume_entries", "resume_version_id,entry_id")},
{fk("block_id,resume_id", "resume_block_owners", "block_id,resume_id")})""",
    ),
    (
        "default_resume_selection",
        f"""CREATE TABLE default_resume_selection (
singleton_key INTEGER PRIMARY KEY CHECK(singleton_key=1),
default_resume_id TEXT,
revision INTEGER NOT NULL CHECK(typeof(revision)='integer' AND revision BETWEEN 1 AND 9007199254740991),
CHECK(default_resume_id IS NULL OR (length(default_resume_id)=36 AND lower(default_resume_id)=default_resume_id)),
{fk("default_resume_id", "resumes", "resume_id")})""",
    ),
    (
        "candidate_evidence_projections",
        f"""CREATE TABLE candidate_evidence_projections (
{identity("resume_version_id", True)}, extraction_key TEXT NOT NULL,
{json_column("projection")},
{fk("resume_version_id", "resume_versions", "resume_version_id")})""",
    ),
    (
        "portrait_builds",
        f"""CREATE TABLE portrait_builds (
{identity("build_id", True)}, {identity("source_resume_version_id")},
selection_revision INTEGER NOT NULL CHECK(typeof(selection_revision)='integer' AND selection_revision BETWEEN 1 AND 9007199254740991),
extraction_key TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('QUEUED','RUNNING','SUCCEEDED','FAILED','OBSOLETE')),
failure_code TEXT, {timestamp_column("created_at")},
CHECK((status='FAILED')=(failure_code IS NOT NULL)),
{fk("source_resume_version_id", "resume_versions", "resume_version_id")},
{fk("source_resume_version_id", "candidate_evidence_projections", "resume_version_id")})""",
    ),
    (
        "portraits",
        f"""CREATE TABLE portraits (
{identity("portrait_id", True)}, {identity("resume_version_id")}, extraction_key TEXT NOT NULL,
{json_column("portrait")}, {timestamp_column("created_at")},
{fk("resume_version_id", "candidate_evidence_projections", "resume_version_id")})""",
    ),
    (
        "current_portrait_state",
        f"""CREATE TABLE current_portrait_state (
singleton_key INTEGER PRIMARY KEY CHECK(singleton_key=1), source_resume_version_id TEXT,
status TEXT NOT NULL CHECK(status IN ('NO_SOURCE','EMPTY_SOURCE','QUEUED','RUNNING','READY','FAILED')),
build_id TEXT, portrait_id TEXT, failure_code TEXT,
CHECK((status='NO_SOURCE')=(source_resume_version_id IS NULL)),
CHECK((status IN ('QUEUED','RUNNING','READY','FAILED'))=(build_id IS NOT NULL)),
CHECK((status='READY')=(portrait_id IS NOT NULL)),
CHECK((status='FAILED')=(failure_code IS NOT NULL)),
{fk("source_resume_version_id", "resume_versions", "resume_version_id")},
{fk("build_id", "portrait_builds", "build_id")},
{fk("portrait_id", "portraits", "portrait_id")})""",
    ),
    (
        "candidate_command_receipts",
        f"""CREATE TABLE candidate_command_receipts (
{identity("request_id", True)},
command_type TEXT NOT NULL CHECK(command_type IN ('RESUME_CREATE','RESUME_SAVE','RESUME_RENAME','RESUME_REMOVE','DEFAULT_RESUME_SET','PORTRAIT_REFRESH')),
request_fingerprint TEXT NOT NULL CHECK(length(request_fingerprint)=64 AND request_fingerprint NOT GLOB '*[^0-9a-f]*'),
schema_version INTEGER NOT NULL CHECK(typeof(schema_version)='integer' AND schema_version=2),
outcome TEXT NOT NULL CHECK(outcome IN ('CREATED','UPDATED','REMOVED','UNCHANGED')),
{json_column("result_snapshot")}, resume_id TEXT, resume_version_id TEXT,
default_resume_id TEXT, source_resume_version_id TEXT, build_id TEXT,
{fk("resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")},
{fk("default_resume_id", "resumes", "resume_id")},
{fk("source_resume_version_id", "resume_versions", "resume_version_id")},
{fk("build_id", "portrait_builds", "build_id")})""",
    ),
)


def seed(conn: Connection, fault: Callable[[str], None]) -> None:
    conn.exec_driver_sql("INSERT INTO default_resume_selection VALUES (1,NULL,1)")
    conn.exec_driver_sql(
        "INSERT INTO current_portrait_state VALUES (1,NULL,'NO_SOURCE',NULL,NULL,NULL)"
    )
    fault("migration_independent_resume_seeds")
