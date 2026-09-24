"""Internal deterministic planning and zero-call portrait completion boundary."""

from collections.abc import Callable

from pydantic import TypeAdapter, ValidationError

from jobhunter.application.manual_application_entries.service import utc_now
from jobhunter.domain.profile.incremental import ConfigurationKey
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import UuidV4
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import (
    CandidateRepository,
    Json,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def validated(adapter: TypeAdapter[str], value: str) -> str:
    try:
        return adapter.validate_python(value)
    except ValidationError:
        raise Failure("VALIDATION_ERROR") from None


class PortraitDerivation:
    """Freeze one plan or publish only a proven local zero-call result."""

    def __init__(self, store: Store, *, clock: Callable[[], str] = utc_now) -> None:
        self.store = store
        self.clock = clock

    def plan(self, build_id: str, configuration_key: str) -> Json:
        identity = validated(TypeAdapter[str](UuidV4), build_id)
        configuration = validated(TypeAdapter[str](ConfigurationKey), configuration_key)
        return self.store.run(
            lambda conn: CandidateRepository(conn).build_plan(identity, configuration),
            write=True,
        )

    def complete_zero_call(self, build_id: str) -> Json:
        identity = validated(TypeAdapter[str](UuidV4), build_id)
        return self.store.run(
            lambda conn: CandidateRepository(conn).complete_zero_call(identity, self.clock()),
            write=True,
        )
