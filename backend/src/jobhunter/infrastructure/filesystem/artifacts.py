"""Open verified regular files relative to an owned directory, then serve a snapshot."""

import hashlib
import os
import stat
import tempfile
from pathlib import Path
from typing import BinaryIO

from pydantic import TypeAdapter

from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import UuidV4


class ArtifactFiles:
    def __init__(self, directory: Path) -> None:
        self.directory = directory

    def snapshot(self, artifact_id: str, byte_length: int, sha256: str) -> BinaryIO:
        TypeAdapter[str](UuidV4).validate_python(artifact_id)
        root = child = fd = -1
        snapshot: BinaryIO | None = None
        try:
            root = os.open(self.directory, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            child = os.open("artifacts", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=root)
            fd = os.open(artifact_id, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=child)
            if not stat.S_ISREG(os.fstat(fd).st_mode):
                raise Failure("ARTIFACT_INTEGRITY_FAILED")
            snapshot = tempfile.TemporaryFile(mode="w+b")
            digest = hashlib.sha256()
            total = 0
            while chunk := os.read(fd, 65536):
                total += len(chunk)
                if total > byte_length:
                    raise Failure("ARTIFACT_INTEGRITY_FAILED")
                digest.update(chunk)
                snapshot.write(chunk)
            if total != byte_length or digest.hexdigest() != sha256:
                raise Failure("ARTIFACT_INTEGRITY_FAILED")
            snapshot.seek(0)
            return snapshot
        except BaseException as exc:
            if snapshot is not None:
                snapshot.close()
            if isinstance(exc, FileNotFoundError):
                raise Failure("ARTIFACT_UNAVAILABLE") from None
            if isinstance(exc, OSError):
                raise Failure("STORAGE_UNAVAILABLE") from None
            raise
        finally:
            for opened in (fd, child, root):
                if opened >= 0:
                    os.close(opened)

    def place(self, identity: str, data: bytes) -> None:
        """Non-overwriting durable bytes first; a later DB rollback leaves a private orphan."""
        import fcntl

        TypeAdapter[str](UuidV4).validate_python(identity)
        root = child = fd = -1
        try:
            root = os.open(self.directory, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            try:
                os.mkdir("artifacts", 0o700, dir_fd=root)
            except FileExistsError:
                pass
            child = os.open("artifacts", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=root)
            os.fchmod(child, 0o700)
            fd = os.open(
                identity, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=child
            )
            view = memoryview(data)
            while view:
                written = os.write(fd, view[:65536])
                view = view[written:]
            os.fsync(fd)
            if hasattr(fcntl, "F_FULLFSYNC"):
                fcntl.fcntl(fd, fcntl.F_FULLFSYNC)
            os.fsync(child)
            os.fsync(root)
        except OSError:
            raise Failure("STORAGE_UNAVAILABLE") from None
        finally:
            for opened in (fd, child, root):
                if opened >= 0:
                    os.close(opened)
