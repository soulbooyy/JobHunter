"""Add Preferences authority and receipts without rewriting schema 1."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import TABLES

revision = "cd891047a2e6"
down_revision = "b720a94fd381"
branch_labels = None
depends_on = None


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    for name, ddl in TABLES:
        op.execute(ddl)
        fault("migration_" + name)
    op.execute("PRAGMA user_version=2")
    fault("migration_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
