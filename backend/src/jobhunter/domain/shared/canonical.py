"""COM-045 shared typed value encoding; consumers retain their own prefixes."""

from decimal import Decimal
from typing import cast


def encode(value: object) -> bytes:
    if value is None:
        return b"n"
    if isinstance(value, bool):
        return b"b1" if value else b"b0"
    if isinstance(value, str):
        raw = value.encode("utf-8")
        return b"s" + str(len(raw)).encode() + b":" + raw
    if isinstance(value, (int, Decimal, float)):
        number = Decimal(str(value))
        if not number.is_finite():
            raise ValueError("Non-finite number")
        text = format(number, "f") if number else "0"
        if "." in text:
            text = text.rstrip("0").rstrip(".")
        raw = text.encode("ascii")
        return b"d" + str(len(raw)).encode() + b":" + raw
    if isinstance(value, list):
        values = cast(list[object], value)
        return b"a" + str(len(values)).encode() + b":" + b"".join(encode(v) for v in values)
    if isinstance(value, dict):
        values = cast(dict[str, object], value)
        return (
            b"o"
            + str(len(values)).encode()
            + b":"
            + b"".join(encode(k) + encode(values[k]) for k in sorted(values))
        )
    raise TypeError("Unsupported canonical value")
