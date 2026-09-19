"""SL-01.M1 initial application schema. Initialization only; never auto-upgrade."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    APPLICATION_ID,
    ENTRY_DDL,
    RECEIPT_DDL,
)

revision = "b720a94fd381"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    op.execute(ENTRY_DDL)
    fault("initialization_entry")
    op.execute(RECEIPT_DDL)
    fault("initialization_receipt")
    op.execute(f"PRAGMA application_id = {APPLICATION_ID}")
    fault("initialization_identity")
    op.execute("PRAGMA user_version = 1")
    fault("initialization_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
