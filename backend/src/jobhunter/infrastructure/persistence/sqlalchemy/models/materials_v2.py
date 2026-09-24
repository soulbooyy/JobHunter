"""Schema-6 material persistence over exact independent ResumeVersion sources."""

# ruff: noqa: E501 -- exact versioned SQLite DDL is kept visually comparable.

from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v2 import fk, json_column
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials import (
    FAILURES,
    LIMIT_NAMES,
    optional_identity,
    optional_timestamp,
    positive,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import identity
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import timestamp_column

TABLES: tuple[tuple[str, str], ...] = (
    (
        "render_configurations",
        f"""CREATE TABLE render_configurations (
{identity("render_configuration_id", True)}, {json_column("configuration")})""",
    ),
    (
        "render_work",
        f"""CREATE TABLE render_work (
{identity("work_id", True)}, {identity("resume_version_id")}, {identity("render_configuration_id")},
status TEXT NOT NULL CHECK(status IN ('QUEUED','RUNNING','SUCCEEDED','FAILED')),
attempt_count INTEGER NOT NULL CHECK(typeof(attempt_count)='integer' AND attempt_count>=0),
{", ".join(positive(name) for name in LIMIT_NAMES)},
{optional_identity("current_attempt_id")}, {timestamp_column("created_at")},
{optional_timestamp("finished_at")}, {optional_identity("artifact_id")},
failure_code TEXT CHECK(failure_code IN ({FAILURES})),
CHECK(attempt_count<=max_attempts), CHECK((status='RUNNING')=(current_attempt_id IS NOT NULL)),
CHECK((status IN ('SUCCEEDED','FAILED'))=(finished_at IS NOT NULL)),
CHECK((status='SUCCEEDED')=(artifact_id IS NOT NULL)), CHECK((status='FAILED')=(failure_code IS NOT NULL)),
CHECK(status NOT IN ('RUNNING','SUCCEEDED') OR attempt_count>0),
UNIQUE(work_id,resume_version_id,render_configuration_id), UNIQUE(work_id,status,artifact_id),
UNIQUE(work_id,artifact_id), UNIQUE(work_id,failure_code), UNIQUE(work_id,finished_at),
{fk("resume_version_id", "resume_versions", "resume_version_id")},
{fk("render_configuration_id", "render_configurations", "render_configuration_id")},
{fk("artifact_id,work_id", "artifacts", "artifact_id,creating_work_id")})""",
    ),
    (
        "artifacts",
        f"""CREATE TABLE artifacts (
{identity("artifact_id", True)}, schema_version INTEGER NOT NULL CHECK(schema_version=2),
{identity("creating_work_id")}, creator_status TEXT NOT NULL CHECK(creator_status='SUCCEEDED'),
{identity("resume_id")}, {identity("resume_version_id")}, {identity("render_configuration_id")},
media_type TEXT NOT NULL CHECK(media_type IN ('application/pdf','image/png')),
{positive("byte_length")}, sha256 TEXT NOT NULL CHECK(length(sha256)=64 AND sha256 NOT GLOB '*[^0-9a-f]*'),
{timestamp_column("created_at")}, CHECK(byte_length<=9007199254740991),
UNIQUE(artifact_id,resume_version_id), UNIQUE(creating_work_id), UNIQUE(artifact_id,creating_work_id),
UNIQUE(artifact_id,resume_version_id,render_configuration_id),
{fk("creating_work_id,creator_status,artifact_id", "render_work", "work_id,status,artifact_id")},
{fk("creating_work_id,resume_version_id,render_configuration_id", "render_work", "work_id,resume_version_id,render_configuration_id")},
{fk("resume_version_id,resume_id", "resume_versions", "resume_version_id,resume_id")},
{fk("render_configuration_id", "render_configurations", "render_configuration_id")})""",
    ),
    (
        "render_intents",
        f"""CREATE TABLE render_intents (
{identity("render_intent_id", True)}, {identity("resume_version_id")},
{identity("render_configuration_id")}, status TEXT NOT NULL CHECK(status IN ('PENDING','FULFILLED','FAILED')),
{timestamp_column("created_at")}, {optional_timestamp("finished_at")}, {optional_identity("artifact_id")},
failure_code TEXT CHECK(failure_code IN ({FAILURES})), {optional_identity("work_id")},
CHECK((status!='PENDING')=(finished_at IS NOT NULL)), CHECK((status='FULFILLED')=(artifact_id IS NOT NULL)),
CHECK((status='FAILED')=(failure_code IS NOT NULL)), CHECK(status='FULFILLED' OR work_id IS NOT NULL),
UNIQUE(render_intent_id,resume_version_id,render_configuration_id),
{fk("resume_version_id", "resume_versions", "resume_version_id")},
{fk("render_configuration_id", "render_configurations", "render_configuration_id")},
{fk("work_id,resume_version_id,render_configuration_id", "render_work", "work_id,resume_version_id,render_configuration_id")},
{fk("artifact_id,resume_version_id,render_configuration_id", "artifacts", "artifact_id,resume_version_id,render_configuration_id")},
{fk("work_id,artifact_id", "render_work", "work_id,artifact_id")},
{fk("work_id,failure_code", "render_work", "work_id,failure_code")},
{fk("work_id,finished_at", "render_work", "work_id,finished_at")})""",
    ),
    (
        "material_command_receipts",
        f"""CREATE TABLE material_command_receipts (
{identity("request_id")}, operation TEXT NOT NULL CHECK(operation='RENDER_REQUEST'),
request_fingerprint TEXT NOT NULL CHECK(length(request_fingerprint)=64 AND request_fingerprint NOT GLOB '*[^0-9a-f]*'),
schema_version INTEGER NOT NULL CHECK(schema_version=1), {json_column("result_snapshot")},
{identity("render_intent_id")}, PRIMARY KEY(operation,request_id), UNIQUE(render_intent_id),
{fk("render_intent_id", "render_intents", "render_intent_id")})""",
    ),
)

INDEXES = (
    (
        "one_unfinished_render_work",
        "CREATE UNIQUE INDEX one_unfinished_render_work ON render_work(resume_version_id,render_configuration_id) WHERE status IN ('QUEUED','RUNNING')",
    ),
)
