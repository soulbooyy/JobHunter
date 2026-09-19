# Narrow declarations for the two verified urlstd APIs consumed by M1.
class ValidityState:
    def __init__(self, *, disable_logging: bool = True) -> None: ...

class URLValidator:
    @classmethod
    def is_valid(cls, urlstring: str, *, validity: ValidityState) -> bool: ...

class Host:
    @classmethod
    def parse(cls, host: str, *, validity: ValidityState) -> str | int | tuple[int, ...]: ...
