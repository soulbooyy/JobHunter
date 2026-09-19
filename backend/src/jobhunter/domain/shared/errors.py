"""Shared sanitized operation failure."""


class Failure(Exception):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)

    def body(self) -> dict[str, object]:
        return {
            "code": self.code,
            "message": (
                "Unsupported storage schema; schema 1 requires explicit offline migration."
                if self.code == "SCHEMA_UNSUPPORTED"
                else self.code.replace("_", " ").capitalize() + "."
            ),
            "field_errors": [],
        }
