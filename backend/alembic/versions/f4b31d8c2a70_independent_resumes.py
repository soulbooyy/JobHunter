"""Replace disposable development Candidate/Materials data with independent Resumes."""

from collections.abc import Callable
from typing import cast

from alembic import op
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate_v2 import TABLES, seed
from jobhunter.infrastructure.persistence.sqlalchemy.models.invocation import (
    TABLES as INVOCATION_TABLES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials_v2 import (
    INDEXES as MATERIAL_INDEXES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.materials_v2 import (
    TABLES as MATERIAL_TABLES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import (
    TABLES as PREFERENCE_TABLES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    ENTRY_DDL,
    ENTRY_TABLE,
    RECEIPT_DDL,
    RECEIPT_TABLE,
)

revision = "f4b31d8c2a70"
down_revision = "d092ea64bf17"
branch_labels = None
depends_on = None

OLD_TABLES = (
    "controlled_model_proofs",
    "controlled_local_reads",
    "invocation_responses",
    "model_invocations",
    "agent_runs",
    "material_command_receipts",
    "render_intents",
    "artifact_sources",
    "artifacts",
    "render_work",
    "render_configurations",
    "candidate_command_receipts",
    "default_resume_selection",
    "resume_members",
    "resume_sections",
    "resume_versions",
    "resumes",
    "current_evidence_baseline",
    "evidence_baseline_members",
    "evidence_baselines",
    "evidence_item_versions",
    "evidence_items",
    "profile_versions",
    "profiles",
    "preference_save_receipts",
    "preference_set_versions",
    "preference_sets",
    "manual_application_entry_create_receipts",
    "manual_application_entries",
)


def upgrade() -> None:
    config = op.get_context().config
    assert config is not None
    fault = cast(Callable[[str], None], config.attributes["fault"])
    op.execute("PRAGMA defer_foreign_keys=ON")
    for table in OLD_TABLES:
        op.execute(f"DELETE FROM {table}")
    for table in OLD_TABLES:
        op.execute(f"DROP TABLE {table}")
        fault("migration_drop_" + table)
    for name, ddl in (
        (ENTRY_TABLE, ENTRY_DDL),
        (RECEIPT_TABLE, RECEIPT_DDL),
        *PREFERENCE_TABLES,
        *INVOCATION_TABLES,
        *TABLES,
    ):
        op.execute(ddl)
        fault("migration_" + name)
    seed(op.get_bind(), fault)
    for name, ddl in (*MATERIAL_TABLES, *MATERIAL_INDEXES):
        op.execute(ddl)
        fault("migration_" + name)
    op.execute("PRAGMA user_version=6")
    fault("migration_independent_resume_version")


def downgrade() -> None:
    raise RuntimeError("Destructive downgrade is not supported.")
