"""Private subprocess entry; inherited ownership FD fences parent-crash recovery."""

import json
import os
import sys
from pathlib import Path

from jobhunter.domain.derived_work.models import Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.rendering.pipeline import render


def main() -> None:
    try:
        request = json.load(sys.stdin)
        result = render(
            MaterialSource.model_validate(request["source"]),
            RenderConfiguration.model_validate(request["configuration"]),
            Work.model_validate(request["work"]),
            Path(request["fonts"]),
            request["manifest"],
        )
        fd = int(sys.argv[1])
        view = memoryview(result)
        while view:
            count = os.write(fd, view[:65536])
            view = view[count:]
        print("OK", flush=True)
    except Failure as exc:
        print(exc.code, flush=True)
    except PermissionError:
        print("PERMISSION_DENIED", flush=True)
    except Exception:
        print("RENDER_FAILED", flush=True)


if __name__ == "__main__":
    main()
