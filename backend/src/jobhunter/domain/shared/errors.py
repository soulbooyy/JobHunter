"""Shared sanitized operation failure."""


class Failure(Exception):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)

    def body(self) -> dict[str, object]:
        return {
            "code": self.code,
            "message": self.code.replace("_", " ").capitalize() + ".",
            "field_errors": [],
        }
