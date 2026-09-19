"""Immutable schema-2 additions; schema-1 definitions remain unchanged."""

from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    timestamp_column,
    uuid_check,
)

ALEMBIC_REVISION = "cd891047a2e6"


def identity(name: str, primary: bool = False) -> str:
    return (
        f"{name} TEXT COLLATE BINARY {'PRIMARY KEY ' if primary else ''}NOT NULL "
        f"CHECK({uuid_check(name)})"
    )


def revision(name: str) -> str:
    return (
        f"{name} INTEGER NOT NULL CHECK(typeof({name})='integer' "
        f"AND {name} BETWEEN 1 AND 9007199254740991)"
    )


ROOT_DDL = f"""CREATE TABLE preference_sets (
{identity("preference_set_id", True)},
singleton_key INTEGER NOT NULL UNIQUE CHECK(typeof(singleton_key)='integer' AND singleton_key=1),
{identity("current_preference_set_version_id")},
{revision("revision")},
{timestamp_column("created_at")},
{timestamp_column("updated_at")},
CHECK(updated_at >= created_at),
FOREIGN KEY (current_preference_set_version_id, preference_set_id)
REFERENCES preference_set_versions(preference_set_version_id, preference_set_id)
DEFERRABLE INITIALLY DEFERRED
)"""
VERSION_DDL = f"""CREATE TABLE preference_set_versions (
{identity("preference_set_version_id", True)},
{identity("preference_set_id")},
{timestamp_column("created_at")},
configuration TEXT NOT NULL CHECK(typeof(configuration)='text' AND json_valid(configuration)
AND json_type(configuration)='object'),
UNIQUE(preference_set_version_id, preference_set_id),
FOREIGN KEY (preference_set_id) REFERENCES preference_sets(preference_set_id)
DEFERRABLE INITIALLY DEFERRED
)"""
RECEIPT_DDL = f"""CREATE TABLE preference_save_receipts (
{identity("request_id", True)},
request_fingerprint TEXT COLLATE BINARY NOT NULL CHECK(typeof(request_fingerprint)='text'
AND length(request_fingerprint)=64 AND request_fingerprint NOT GLOB '*[^0-9a-f]*'),
{identity("preference_set_id")},
{identity("preference_set_version_id")},
{revision("result_revision")},
outcome TEXT COLLATE BINARY NOT NULL CHECK(typeof(outcome)='text'
AND outcome IN ('CREATED', 'UPDATED', 'UNCHANGED')),
FOREIGN KEY (preference_set_version_id, preference_set_id)
REFERENCES preference_set_versions(preference_set_version_id, preference_set_id)
DEFERRABLE INITIALLY DEFERRED
)"""
TABLES = (
    ("preference_sets", ROOT_DDL),
    ("preference_set_versions", VERSION_DDL),
    ("preference_save_receipts", RECEIPT_DDL),
)
