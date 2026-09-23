"""One isolated producer process; file/OS mechanics never publish canonical records."""

import json
import os
import subprocess
import sys
import tempfile
import time
from collections.abc import Callable
from pathlib import Path

from jobhunter.domain.derived_work.models import Work
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json


class ProcessRenderer:
    def __init__(
        self, assets: Path, environment: Callable[[], dict[str, str]], lock_fd: int
    ) -> None:
        self.assets, self.environment, self.lock_fd = assets, environment, lock_fd

    def produce(
        self,
        source: MaterialSource,
        configuration: Json,
        work: Work,
        deadline: float,
        on_timeout: Callable[[], None],
    ) -> bytes:
        request = json.dumps(
            {
                "source": source.model_dump(mode="json"),
                "configuration": configuration,
                "work": work.model_dump(mode="json"),
                "fonts": str(self.assets / "fonts"),
                "manifest": json.loads((self.assets / "font-manifest.json").read_text()),
            }
        ).encode("utf-8")
        with tempfile.TemporaryFile(mode="w+b") as candidate:
            process = subprocess.Popen(
                [
                    sys.executable,
                    "-m",
                    "jobhunter.infrastructure.rendering.worker",
                    str(candidate.fileno()),
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                pass_fds=(candidate.fileno(), self.lock_fd),
                env=self.environment(),
            )
            try:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise subprocess.TimeoutExpired(process.args, 0)
                output, _ = process.communicate(request, timeout=remaining)
            except subprocess.TimeoutExpired:
                try:
                    on_timeout()
                finally:
                    process.terminate()
                    try:
                        process.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    process.communicate()
                raise Failure("RESOURCE_LIMIT_EXCEEDED") from None
            if process.returncode != 0:
                raise Failure("RENDER_FAILED")
            code = output.decode("ascii", errors="replace").strip()
            if code != "OK":
                allowed = {
                    "CONFIGURATION_UNAVAILABLE",
                    "PERMISSION_DENIED",
                    "OUTPUT_INVALID",
                    "RESOURCE_LIMIT_EXCEEDED",
                    "RENDER_FAILED",
                }
                raise Failure(code if code in allowed else "RENDER_FAILED")
            candidate.seek(0, os.SEEK_END)
            if candidate.tell() > work.max_output_bytes or time.monotonic() >= deadline:
                raise Failure("RESOURCE_LIMIT_EXCEEDED")
            candidate.seek(0)
            data = candidate.read(work.max_output_bytes + 1)
            if not data:
                raise Failure("OUTPUT_INVALID")
            return data
