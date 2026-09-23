"""Internal invocation durability; no backfilled execution history."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.invocation import TABLES

revision = "d092ea64bf17"
down_revision = "a41d7e90c263"
branch_labels = None
depends_on = None


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    for name, ddl in TABLES:
        op.execute(ddl)
        fault("migration_" + name)
    op.execute("PRAGMA user_version=5")
    fault("migration_invocation_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
