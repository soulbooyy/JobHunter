"""Immutable M1 schema specification used by migration and recognition."""

APPLICATION_ID = 0x4A484E54
SCHEMA_VERSION = 1
ALEMBIC_REVISION = "b720a94fd381"
ENTRY_TABLE = "manual_application_entries"
RECEIPT_TABLE = "manual_application_entry_create_receipts"


def uuid_check(column: str) -> str:
    pattern = "[0-9a-f]" * 8 + "-" + "[0-9a-f]" * 4 + "-4" + "[0-9a-f]" * 3
    pattern += "-[89ab]" + "[0-9a-f]" * 3 + "-" + "[0-9a-f]" * 12
    return f"typeof({column}) = 'text' AND length({column}) = 36 AND {column} GLOB '{pattern}'"


def text_column(name: str, maximum: int) -> str:
    return (
        f"{name} TEXT COLLATE BINARY NOT NULL CHECK(typeof({name}) = 'text' "
        f"AND length({name}) BETWEEN 1 AND {maximum})"
    )


def timestamp_column(name: str) -> str:
    digit = "[0-9]"
    pattern = digit * 4 + "-" + digit * 2 + "-" + digit * 2
    pattern += "T" + digit * 2 + ":" + digit * 2 + ":" + digit * 2 + "." + digit * 3 + "Z"
    return (
        f"{name} TEXT COLLATE BINARY NOT NULL CHECK(typeof({name}) = 'text' "
        f"AND length({name}) = 24 AND {name} GLOB '{pattern}')"
    )


ENTRY_DDL = f"""CREATE TABLE {ENTRY_TABLE} (
manual_application_entry_id TEXT COLLATE BINARY PRIMARY KEY NOT NULL
CHECK({uuid_check("manual_application_entry_id")}),
{text_column("company_name", 200)},
{text_column("role_title", 200)},
{text_column("application_url", 8192)},
revision INTEGER NOT NULL CHECK(typeof(revision) = 'integer'
AND revision BETWEEN 1 AND 9007199254740991),
{timestamp_column("created_at")},
{timestamp_column("updated_at")},
CHECK(updated_at >= created_at)
)"""
RECEIPT_DDL = f"""CREATE TABLE {RECEIPT_TABLE} (
request_id TEXT COLLATE BINARY PRIMARY KEY NOT NULL CHECK({uuid_check("request_id")}),
request_fingerprint TEXT COLLATE BINARY NOT NULL CHECK(typeof(request_fingerprint) = 'text'
AND length(request_fingerprint) = 64 AND request_fingerprint NOT GLOB '*[^0-9a-f]*'),
manual_application_entry_id TEXT COLLATE BINARY NOT NULL UNIQUE
CHECK({uuid_check("manual_application_entry_id")})
)"""

ALEMBIC_DDL = """CREATE TABLE alembic_version (
version_num VARCHAR(32) NOT NULL,
CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
)"""
