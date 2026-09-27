"""Remove the retired Invocation runtime schema and its Candidate reference."""

from collections.abc import Callable
from typing import Any, cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v4 import (
    PORTRAIT_BUILD_DDL,
    ddl,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.invocation import TABLES
from sqlalchemy.engine import Connection

revision = "6f2a7c9d4e10"
down_revision = "8c92f0d4ae31"
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
        fault("migration_remove_invocation_drop_" + table)

    op.execute(PORTRAIT_BUILD_DDL)
    fault("migration_remove_invocation_portrait_builds")
    for row in builds:
        row.pop("run_id")
        insert(conn, "portrait_builds", row)

    op.execute(ddl("current_portrait_state"))
    fault("migration_remove_invocation_current_portrait_state")
    insert(conn, "current_portrait_state", state)
    op.execute(ddl("candidate_command_receipts"))
    fault("migration_remove_invocation_candidate_command_receipts")
    for row in receipts:
        insert(conn, "candidate_command_receipts", row)

    for table, _ in reversed(TABLES):
        op.execute(f"DROP TABLE {table}")
        fault("migration_remove_invocation_drop_" + table)

    op.execute("PRAGMA user_version=8")
    fault("migration_remove_invocation_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
