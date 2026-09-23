"""Schema 3: relational retained authority and command-result lineage."""

from collections.abc import Callable
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy.engine import Connection

from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import identity, revision
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import timestamp_column

ALEMBIC_REVISION = "ef03c92ba671"
KINDS = "'EDUCATION','WORK_EXPERIENCE','PROJECT','SKILL','AWARD','CERTIFICATION'"


def json_column(name: str, kind: str = "object") -> str:
    return (
        f"{name} TEXT NOT NULL CHECK(typeof({name})='text' AND json_valid({name}) "
        f"AND json_type({name})='{kind}')"
    )


def fk(columns: str, table: str, targets: str) -> str:
    return f"FOREIGN KEY ({columns}) REFERENCES {table}({targets}) DEFERRABLE INITIALLY DEFERRED"


def owner_fk(name: str, current: bool = False) -> str:
    columns = name + "_version_id," + name + "_id"
    return fk(("current_" if current else "") + columns, name + "_versions", columns)


def root(name: str, extra: str) -> str:
    return f"""CREATE TABLE {name}s (
{identity(name + "_id", True)}, {extra},
{identity("current_" + name + "_version_id")}, {revision("revision")},
{timestamp_column("created_at")}, {timestamp_column("updated_at")},
{("UNIQUE(evidence_item_id,kind)," if name == "evidence_item" else "")}
CHECK(updated_at >= created_at),
{owner_fk(name, current=True)}
)"""


def version(name: str, extra: str) -> str:
    return f"""CREATE TABLE {name}_versions (
{identity(name + "_version_id", True)}, {identity(name + "_id")},
schema_version INTEGER NOT NULL CHECK(typeof(schema_version)='integer' AND schema_version=1),
{timestamp_column("created_at")}, {extra},
UNIQUE({name}_version_id, {name}_id),
{fk(name + "_id", name + "s", name + "_id")}
)"""


TABLES: tuple[tuple[str, str], ...] = (
    (
        "profiles",
        root(
            "profile",
            (
                "singleton_key INTEGER NOT NULL UNIQUE CHECK(singleton_key=1 AND "
                "typeof(singleton_key)='integer')"
            ),
        ),
    ),
    ("profile_versions", version("profile", "full_name TEXT, phone_number TEXT, email TEXT")),
    (
        "evidence_items",
        root(
            "evidence_item",
            f"kind TEXT NOT NULL CHECK(kind IN ({KINDS})), "
            "status TEXT NOT NULL CHECK(status IN ('ACTIVE','RETIRED'))",
        ),
    ),
    (
        "evidence_item_versions",
        version("evidence_item", json_column("fields") + ", " + json_column("content", "array")),
    ),
    (
        "evidence_baselines",
        f"""CREATE TABLE evidence_baselines (
{identity("evidence_baseline_snapshot_id", True)}, schema_version INTEGER
NOT NULL CHECK(schema_version=1 AND typeof(schema_version)='integer'),
{timestamp_column("created_at")})""",
    ),
    (
        "evidence_baseline_members",
        f"""CREATE TABLE evidence_baseline_members (
{identity("evidence_baseline_snapshot_id")}, {identity("evidence_item_id")},
{identity("evidence_item_version_id")},
PRIMARY KEY(evidence_baseline_snapshot_id,evidence_item_id),
{fk("evidence_baseline_snapshot_id", "evidence_baselines", "evidence_baseline_snapshot_id")},
{owner_fk("evidence_item")})""",
    ),
    (
        "current_evidence_baseline",
        f"""CREATE TABLE current_evidence_baseline (
singleton_key INTEGER PRIMARY KEY CHECK(singleton_key=1),
{identity("evidence_baseline_snapshot_id")},
{fk("evidence_baseline_snapshot_id", "evidence_baselines", "evidence_baseline_snapshot_id")})""",
    ),
    (
        "resumes",
        root(
            "resume",
            (
                "resume_name TEXT NOT NULL CHECK(typeof(resume_name)='text'), status TEXT NOT "
                "NULL CHECK(status IN ('ACTIVE','REMOVED'))"
            ),
        ),
    ),
    (
        "resume_versions",
        version(
            "resume",
            f"{identity('profile_version_id')}, {json_column('header_presentation')}, "
            f"{json_column('document_presentation')}, "
            f"{fk('profile_version_id', 'profile_versions', 'profile_version_id')}",
        ),
    ),
    (
        "resume_sections",
        f"""CREATE TABLE resume_sections (
{identity("resume_version_id")}, position INTEGER NOT NULL CHECK(typeof(position)='integer'
AND position BETWEEN 0 AND 5), kind TEXT NOT NULL CHECK(kind IN ({KINDS})),
PRIMARY KEY(resume_version_id,position), UNIQUE(resume_version_id,kind),
UNIQUE(resume_version_id,position,kind),
{fk("resume_version_id", "resume_versions", "resume_version_id")})""",
    ),
    (
        "resume_members",
        f"""CREATE TABLE resume_members (
{identity("resume_version_id")}, section_position INTEGER NOT NULL
CHECK(typeof(section_position)='integer'),
position INTEGER NOT NULL CHECK(typeof(position)='integer' AND position BETWEEN 0 AND 99),
kind TEXT NOT NULL CHECK(kind IN ({KINDS})), {identity("evidence_item_id")},
{identity("evidence_item_version_id")}, {json_column("content", "array")},
PRIMARY KEY(resume_version_id,section_position,position),
UNIQUE(resume_version_id,evidence_item_id),
{
            fk(
                "resume_version_id,section_position,kind",
                "resume_sections",
                "resume_version_id,position,kind",
            )
        },
{fk("evidence_item_id,kind", "evidence_items", "evidence_item_id,kind")},
{owner_fk("evidence_item")})""",
    ),
    (
        "default_resume_selection",
        f"""CREATE TABLE default_resume_selection (
singleton_key INTEGER PRIMARY KEY CHECK(singleton_key=1), default_resume_id
TEXT, {revision("revision")},
{fk("default_resume_id", "resumes", "resume_id")})""",
    ),
    (
        "candidate_command_receipts",
        f"""CREATE TABLE candidate_command_receipts (
{identity("request_id", True)},
command_type TEXT NOT NULL CHECK(command_type IN (
'PROFILE_SAVE','EVIDENCE_CREATE','EVIDENCE_UPDATE','EVIDENCE_RETIRE',
'RESUME_CREATE','RESUME_SAVE','RESUME_RENAME','RESUME_REMOVE','DEFAULT_RESUME_SET')),
request_fingerprint TEXT NOT NULL CHECK(typeof(request_fingerprint)='text'
AND length(request_fingerprint)=64 AND request_fingerprint NOT GLOB
'*[^0-9a-f]*'),
schema_version INTEGER NOT NULL CHECK(schema_version=1 AND typeof(schema_version)='integer'),
outcome TEXT NOT NULL CHECK(outcome IN ('CREATED','UPDATED','RETIRED','REMOVED','UNCHANGED')),
{json_column("result_snapshot")},
profile_id TEXT, profile_version_id TEXT, evidence_item_id TEXT, evidence_item_version_id TEXT,
evidence_baseline_snapshot_id TEXT, resume_id TEXT, resume_version_id TEXT, default_resume_id TEXT,
CHECK((command_type='PROFILE_SAVE' AND profile_id IS NOT NULL AND profile_version_id
IS NOT NULL AND evidence_item_id IS NULL AND evidence_item_version_id
IS NULL AND evidence_baseline_snapshot_id IS NULL AND resume_id IS
NULL AND resume_version_id IS NULL AND default_resume_id IS NULL AND
outcome IN ('UPDATED','UNCHANGED'))
OR (command_type IN ('EVIDENCE_CREATE','EVIDENCE_UPDATE','EVIDENCE_RETIRE')
AND evidence_item_id IS NOT NULL AND evidence_item_version_id IS NOT
NULL AND evidence_baseline_snapshot_id IS NOT NULL AND profile_id IS
NULL AND profile_version_id IS NULL AND resume_id IS NULL AND resume_version_id
IS NULL AND default_resume_id IS NULL AND ((command_type='EVIDENCE_CREATE'
AND outcome='CREATED') OR (command_type='EVIDENCE_UPDATE' AND outcome
IN ('UPDATED','UNCHANGED')) OR (command_type='EVIDENCE_RETIRE' AND
outcome IN ('RETIRED','UNCHANGED'))))
OR (command_type IN ('RESUME_CREATE','RESUME_SAVE','RESUME_RENAME','RESUME_REMOVE')
AND resume_id IS NOT NULL AND resume_version_id IS NOT NULL AND profile_id
IS NULL AND profile_version_id IS NULL AND evidence_item_id IS NULL
AND evidence_item_version_id IS NULL AND evidence_baseline_snapshot_id
IS NULL AND (command_type IN ('RESUME_CREATE','RESUME_REMOVE') OR default_resume_id
IS NULL) AND ((command_type='RESUME_CREATE' AND outcome='CREATED')
OR (command_type IN ('RESUME_SAVE','RESUME_RENAME') AND outcome IN
('UPDATED','UNCHANGED')) OR (command_type='RESUME_REMOVE' AND outcome
IN ('REMOVED','UNCHANGED'))))
OR (command_type='DEFAULT_RESUME_SET' AND default_resume_id IS NOT
NULL AND profile_id IS NULL AND profile_version_id IS NULL AND evidence_item_id
IS NULL AND evidence_item_version_id IS NULL AND evidence_baseline_snapshot_id
IS NULL AND resume_id IS NULL AND resume_version_id IS NULL AND outcome
IN ('UPDATED','UNCHANGED'))),
{fk("profile_version_id,profile_id", "profile_versions", "profile_version_id,profile_id")},
{owner_fk("evidence_item")},
{fk("evidence_baseline_snapshot_id", "evidence_baselines", "evidence_baseline_snapshot_id")},
{fk("resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")},
{fk("default_resume_id", "resumes", "resume_id")})""",
    ),
)


def seed(conn: Connection, fault: Callable[[str], None]) -> None:
    now = datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    profile_id, version_id, baseline_id = (str(uuid4()) for _ in range(3))
    conn.exec_driver_sql(
        "INSERT INTO profiles VALUES (?,1,?,1,?,?)", (profile_id, version_id, now, now)
    )
    conn.exec_driver_sql(
        "INSERT INTO profile_versions VALUES (?,?,1,?,NULL,NULL,NULL)",
        (version_id, profile_id, now),
    )
    fault("migration_profile_seed")
    conn.exec_driver_sql("INSERT INTO evidence_baselines VALUES (?,1,?)", (baseline_id, now))
    conn.exec_driver_sql("INSERT INTO current_evidence_baseline VALUES (1,?)", (baseline_id,))
    conn.exec_driver_sql("INSERT INTO default_resume_selection VALUES (1,NULL,1)")
    fault("migration_candidate_seeds")
