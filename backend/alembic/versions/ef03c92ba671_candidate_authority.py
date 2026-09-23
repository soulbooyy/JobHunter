"""Retained Profile, Evidence and Resume authority with atomic receipts."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate import TABLES, seed

revision = "ef03c92ba671"
down_revision = "cd891047a2e6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    for name, ddl in TABLES:
        op.execute(ddl)
        fault("migration_" + name)
    seed(op.get_bind(), fault)
    op.execute("PRAGMA user_version=3")
    fault("migration_candidate_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
