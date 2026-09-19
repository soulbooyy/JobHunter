"""Only a bootstrap-owned connection may run initialization."""

from alembic import context
from sqlalchemy.engine import Connection

connection = context.config.attributes.get("connection")
if not isinstance(connection, Connection):
    raise RuntimeError("Use the JobHunter bootstrap; standalone migration is disabled.")
context.configure(connection=connection, transactional_ddl=True)
context.run_migrations()
