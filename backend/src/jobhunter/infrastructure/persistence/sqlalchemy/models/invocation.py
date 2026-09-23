"""Schema 5: relational execution authority and exact BLOB recovery evidence."""

from sqlalchemy.engine import Connection

from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate import fk
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials import (
    optional_identity,
    optional_timestamp,
    positive,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import identity
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import timestamp_column

ALEMBIC_REVISION = "d092ea64bf17"
SCHEMA_VERSION = 5

TABLES: tuple[tuple[str, str], ...] = (
    (
        "agent_runs",
        f"""CREATE TABLE agent_runs (
{identity("run_id", True)}, consumer_key TEXT NOT NULL CHECK(length(consumer_key)>0),
run_status TEXT NOT NULL CHECK(run_status IN ('OPEN','ENDED')),
execution_generation INTEGER NOT NULL CHECK(typeof(execution_generation)='integer'
AND execution_generation BETWEEN 0 AND 9007199254740991),
{optional_identity("owner_runtime_instance_id")}, {optional_timestamp("deadline_at")},
{timestamp_column("created_at")}, {optional_timestamp("ended_at")},
end_reason TEXT CHECK(end_reason IN
('COMPLETED','FAILED','CANCELLED','TIMED_OUT','OUTCOME_UNKNOWN')),
failure_code TEXT CHECK(length(failure_code)>0),
CHECK(owner_runtime_instance_id IS NULL OR (run_status='OPEN' AND execution_generation>0)),
CHECK((run_status='OPEN' AND ended_at IS NULL AND end_reason IS NULL AND failure_code IS NULL)
OR (run_status='ENDED' AND ended_at IS NOT NULL AND end_reason IS NOT NULL
AND owner_runtime_instance_id IS NULL)),
CHECK((end_reason='FAILED' AND failure_code IS NOT NULL)
OR (failure_code IS NULL AND (end_reason IS NULL OR end_reason!='FAILED'))))""",
    ),
    (
        "model_invocations",
        f"""CREATE TABLE model_invocations (
{identity("invocation_id", True)}, {identity("run_id")}, kind TEXT NOT NULL CHECK(kind='MODEL'),
response_format_key TEXT NOT NULL CHECK(length(response_format_key)>0),
max_response_bytes TEXT NOT NULL CHECK(typeof(max_response_bytes)='text'
AND max_response_bytes GLOB '[1-9]*' AND max_response_bytes NOT GLOB '*[^0-9]*'),
durability_phase TEXT NOT NULL CHECK(durability_phase IN
('PREPARED','DISPATCH_INTENT_DURABLE','RESPONSE_DURABLE')),
dispatch_generation INTEGER CHECK(dispatch_generation IS NULL OR
(typeof(dispatch_generation)='integer'
AND dispatch_generation BETWEEN 1 AND 9007199254740991)),
response_rejection_code TEXT CHECK(response_rejection_code='RESPONSE_TOO_LARGE'),
descriptor TEXT CHECK(json_valid(descriptor)),
CHECK((durability_phase='PREPARED' AND dispatch_generation IS NULL AND descriptor IS NULL)
OR (durability_phase!='PREPARED' AND dispatch_generation IS NOT NULL AND
descriptor IS NOT NULL)),
CHECK(response_rejection_code IS NULL OR durability_phase='DISPATCH_INTENT_DURABLE'),
UNIQUE(invocation_id,response_format_key),
{fk("run_id", "agent_runs", "run_id")})""",
    ),
    (
        "invocation_responses",
        f"""CREATE TABLE invocation_responses (
{identity("invocation_id", True)}, response_format_key TEXT NOT NULL,
serialized_payload BLOB NOT NULL CHECK(typeof(serialized_payload)='blob'),
sha256 TEXT NOT NULL CHECK(length(sha256)=64 AND sha256 NOT GLOB '*[^0-9a-f]*'),
{positive("byte_length")},
{
            fk(
                "invocation_id,response_format_key",
                "model_invocations",
                "invocation_id,response_format_key",
            )
        })""",
    ),
    (
        "controlled_local_reads",
        f"""CREATE TABLE controlled_local_reads (
{identity("invocation_id", True)}, {identity("run_id")}, kind TEXT NOT NULL CHECK(kind='TOOL'),
action_key TEXT NOT NULL CHECK(length(action_key)>0), {identity("source_invocation_id")},
{optional_identity("lineage_id")},
result_sha256 TEXT CHECK(length(result_sha256)=64 AND result_sha256 NOT GLOB '*[^0-9a-f]*'),
result_byte_length INTEGER CHECK(result_byte_length IS NULL OR
(typeof(result_byte_length)='integer' AND result_byte_length>0)),
CHECK((result_sha256 IS NULL)=(result_byte_length IS NULL)),
{fk("run_id", "agent_runs", "run_id")},
{fk("source_invocation_id", "model_invocations", "invocation_id")})""",
    ),
    (
        "controlled_model_proofs",
        f"""CREATE TABLE controlled_model_proofs (
{identity("run_id", True)}, {fk("run_id", "agent_runs", "run_id")})""",
    ),
)


def recognize_metadata(conn: Connection) -> None:
    """Validate structure without scanning historical response/descriptor payloads."""
    from jobhunter.domain.invocation.models import LocalRead, ModelInvocation, Run
    from jobhunter.domain.shared.errors import Failure

    try:
        for row in conn.exec_driver_sql("SELECT * FROM agent_runs").mappings():
            Run.model_validate(dict(row))
        columns = ",".join(ModelInvocation.model_fields)
        for row in conn.exec_driver_sql(f"SELECT {columns} FROM model_invocations").mappings():
            values = dict(row)
            values["max_response_bytes"] = int(values["max_response_bytes"])
            ModelInvocation.model_validate(values)
        for row in conn.exec_driver_sql("SELECT * FROM controlled_local_reads").mappings():
            LocalRead.model_validate(dict(row))
    except ValueError:
        raise Failure("STORAGE_CORRUPT") from None
