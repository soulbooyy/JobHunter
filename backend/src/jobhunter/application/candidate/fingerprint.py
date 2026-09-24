"""SAV-020 typed canonical codec for independent Resume commands."""

import hashlib

from jobhunter.domain.shared.canonical import encode as encode


def fingerprint(command_type: str, target: str | None, body: dict[str, object]) -> str:
    content = {key: value for key, value in body.items() if key != "request_id"}
    return hashlib.sha256(
        b"JobHunter:SL02:Command:2\n" + encode([command_type, target, content])
    ).hexdigest()
