"""Small independently revisioned default selection."""

from jobhunter.domain.shared.values import DTO, Revision, UuidV4


class DefaultSelection(DTO):
    default_resume_id: UuidV4 | None
    revision: Revision


class SelectionToken(DTO):
    revision: Revision


class SetDefault(DTO):
    request_id: UuidV4
    revision: Revision
    default_resume_id: UuidV4
