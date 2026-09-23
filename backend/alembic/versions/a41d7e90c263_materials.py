"""Retained exact material demand, publication lineage and execution fences."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials import INDEXES, TABLES

revision = "a41d7e90c263"
down_revision = "ef03c92ba671"
branch_labels = None
depends_on = None


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    for name, ddl in (*TABLES, *INDEXES):
        op.execute(ddl)
        fault("migration_" + name)
    op.execute("PRAGMA user_version=4")
    fault("migration_material_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
