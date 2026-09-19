"""Single-owner SQLite runtime, recognition and outcome-aware transactions."""

import fcntl
import os
import sqlite3
import stat
import sys
from collections.abc import Callable
from pathlib import Path
from types import TracebackType
from typing import Self, cast

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.pool import NullPool

from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    ALEMBIC_DDL,
    ALEMBIC_REVISION,
    APPLICATION_ID,
    ENTRY_DDL,
    ENTRY_TABLE,
    RECEIPT_DDL,
    RECEIPT_TABLE,
)

Fault = Callable[[str], None]


def no_fault(stage: str) -> None:
    pass


def default_directory() -> Path:
    if sys.platform != "darwin":
        raise Failure("DATA_DIRECTORY_UNAVAILABLE")
    return Path.home() / "Library" / "Application Support" / "JobHunter"


class Store:
    def __init__(
        self, directory: Path, lock_fd: int, engine: Engine, outcome: str, fault: Fault
    ) -> None:
        self.directory = directory
        self.lock_fd = lock_fd
        self.engine = engine
        self.outcome = outcome
        self.fault = fault

    @classmethod
    def open(cls, directory: Path | None = None, *, fault: Fault = no_fault) -> Self:
        explicit = directory is not None
        selected = directory if explicit else default_directory()
        assert selected is not None
        lock_fd = -1
        engine: Engine | None = None
        initializing = False
        try:
            if not selected.is_absolute():
                raise Failure("DATA_DIRECTORY_UNAVAILABLE")
            if not selected.exists() and not explicit:
                selected.mkdir(mode=0o700, parents=True)
            directory = selected.resolve(strict=True)
            info = directory.stat()
            if not directory.is_dir() or info.st_uid != os.getuid():
                raise Failure("DATA_DIRECTORY_UNAVAILABLE")
            if not os.access(directory, os.R_OK | os.W_OK | os.X_OK):
                raise Failure("DATA_DIRECTORY_UNAVAILABLE")
            # Physical device/inode identity also covers symlink and spelling aliases.
            lock_root = Path("/tmp") / f"jobhunter-locks-{os.getuid()}"
            lock_root.mkdir(mode=0o700, exist_ok=True)
            lock_info = lock_root.lstat()
            if (
                not stat.S_ISDIR(lock_info.st_mode)
                or lock_info.st_uid != os.getuid()
                or lock_info.st_mode & 0o077
            ):
                raise Failure("DATA_DIRECTORY_UNAVAILABLE")
            lock_fd = os.open(
                lock_root / f"{info.st_dev}-{info.st_ino}.lock",
                os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW,
                0o600,
            )
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise Failure("DATA_DIRECTORY_IN_USE") from None
            initializing = not any(directory.iterdir())
            database = directory / "jobhunter.sqlite3"
            if not initializing and (not database.is_file() or database.is_symlink()):
                raise Failure("STORAGE_NOT_RECOGNIZED")
            directory.chmod(0o700)
            if initializing:
                fd = os.open(database, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
                os.close(fd)
            for item in directory.iterdir():
                if item.name.startswith("jobhunter.sqlite3"):
                    if item.is_symlink() or item.stat().st_uid != os.getuid():
                        raise Failure("STORAGE_UNAVAILABLE")
                    item.chmod(0o600)

            def connect() -> sqlite3.Connection:
                raw = sqlite3.connect(
                    database.as_uri() + "?mode=rw",
                    uri=True,
                    isolation_level=None,
                    check_same_thread=False,
                    timeout=5,
                )
                try:
                    if initializing:
                        raw.execute("PRAGMA journal_mode=DELETE")
                    if raw.execute("PRAGMA journal_mode").fetchone() != ("delete",):
                        raise Failure("STORAGE_UNAVAILABLE")
                    raw.execute("PRAGMA synchronous=EXTRA")
                    raw.execute("PRAGMA fullfsync=ON")
                    if raw.execute("PRAGMA synchronous").fetchone() != (3,):
                        raise Failure("STORAGE_UNAVAILABLE")
                    if raw.execute("PRAGMA fullfsync").fetchone() != (1,):
                        raise Failure("STORAGE_UNAVAILABLE")
                    return raw
                except BaseException:
                    raw.close()
                    raise

            engine = create_engine(
                "sqlite://",
                creator=connect,
                poolclass=NullPool,
                hide_parameters=True,
                echo=False,
            )
            store = cls(
                directory,
                lock_fd,
                engine,
                "INITIALIZED" if initializing else "OPENED",
                fault,
            )
            if initializing:
                with engine.connect() as conn:
                    conn.exec_driver_sql("BEGIN IMMEDIATE")
                    try:
                        config = Config(str(Path(__file__).resolve().parents[6] / "alembic.ini"))
                        config.attributes["connection"] = conn
                        config.attributes["fault"] = fault
                        command.upgrade(config, ALEMBIC_REVISION)
                        fault("initialization_before_commit")
                        conn.commit()
                    except BaseException:
                        conn.rollback()
                        raise
            store.recognize()
            return store
        except BaseException as exc:
            if engine is not None:
                engine.dispose()
            if lock_fd >= 0:
                os.close(lock_fd)
            if isinstance(exc, Failure):
                raise
            if initializing:
                raise Failure("INITIALIZATION_FAILED") from None
            if isinstance(exc, (FileNotFoundError, PermissionError, NotADirectoryError)):
                raise Failure("DATA_DIRECTORY_UNAVAILABLE") from None
            raise Failure("STORAGE_UNAVAILABLE") from None

    def recognize(self) -> None:
        try:
            with self.engine.connect() as conn:
                if conn.exec_driver_sql("PRAGMA integrity_check").scalars().all() != ["ok"]:
                    raise Failure("STORAGE_CORRUPT")
                if conn.exec_driver_sql("PRAGMA application_id").scalar() != APPLICATION_ID:
                    raise Failure("STORAGE_NOT_RECOGNIZED")
                if conn.exec_driver_sql("PRAGMA user_version").scalar() != 1:
                    raise Failure("SCHEMA_UNSUPPORTED")
                for name, ddl in (
                    (ENTRY_TABLE, ENTRY_DDL),
                    (RECEIPT_TABLE, RECEIPT_DDL),
                    ("alembic_version", ALEMBIC_DDL),
                ):
                    sql = conn.exec_driver_sql(
                        "SELECT sql FROM sqlite_master WHERE type=? AND name=?",
                        ("table", name),
                    ).scalar()
                    if not isinstance(sql, str) or " ".join(sql.split()) != " ".join(ddl.split()):
                        raise Failure("STORAGE_NOT_RECOGNIZED")
                version = (
                    conn.exec_driver_sql("SELECT version_num FROM alembic_version").scalars().all()
                )
                if version != [ALEMBIC_REVISION]:
                    raise Failure("STORAGE_NOT_RECOGNIZED")
        except Failure:
            raise
        except Exception as exc:
            original = getattr(exc, "orig", exc)
            code = getattr(original, "sqlite_errorcode", 0)
            if code in (sqlite3.SQLITE_CORRUPT, sqlite3.SQLITE_NOTADB):
                raise Failure("STORAGE_CORRUPT") from None
            if "no such table" in str(original):
                raise Failure("STORAGE_NOT_RECOGNIZED") from None
            raise Failure("STORAGE_UNAVAILABLE") from None

    def run[T](self, operation: Callable[[Connection], T], *, write: bool = False) -> T:
        try:
            conn = self.engine.connect()
        except Exception:
            raise Failure("STORAGE_UNAVAILABLE") from None
        committing = False
        commit_returned = False
        try:
            conn.exec_driver_sql("BEGIN IMMEDIATE" if write else "BEGIN")
            result = operation(conn)
            self.fault("before_commit")
            committing = True
            self.fault("commit_before_driver")
            conn.commit()
            commit_returned = True
            self.fault("commit_after_driver")
            return result
        except Failure:
            conn.rollback()
            raise
        except Exception as exc:
            if committing and write:
                original = getattr(exc, "orig", exc)
                if (
                    not commit_returned
                    and getattr(original, "sqlite_errorcode", None) == sqlite3.SQLITE_BUSY
                ):
                    # SQLite documents failed BUSY COMMIT as still uncommitted.
                    # SQLAlchemy may already have deactivated its transaction wrapper;
                    # confirm rollback through the actual driver, not wrapper state.
                    try:
                        raw = cast(sqlite3.Connection, conn.connection.driver_connection)
                        raw.rollback()
                    except Exception:
                        raise Failure("OUTCOME_UNKNOWN") from None
                    raise Failure("STORAGE_UNAVAILABLE") from None
                raise Failure("OUTCOME_UNKNOWN") from None
            try:
                conn.rollback()
            except Exception:
                raise Failure("OUTCOME_UNKNOWN" if write else "STORAGE_UNAVAILABLE") from None
            raise Failure("STORAGE_UNAVAILABLE") from None
        finally:
            conn.close()

    def close(self) -> None:
        self.engine.dispose()
        if self.lock_fd >= 0:
            os.close(self.lock_fd)
            self.lock_fd = -1

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()
