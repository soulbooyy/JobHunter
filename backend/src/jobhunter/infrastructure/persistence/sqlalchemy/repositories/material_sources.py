"""Exact independent ResumeVersion projection for the renderer."""

from sqlalchemy.engine import Connection

from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import (
    CandidateRepository,
)


class MaterialSources:
    def __init__(self, conn: Connection) -> None:
        self.candidate = CandidateRepository(conn)

    def read(self, resume_version_id: str) -> MaterialSource:
        return MaterialSource.model_validate(
            {"resume_version": self.candidate.version(resume_version_id, required=True)}
        )
