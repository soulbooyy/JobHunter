"""STO-038 projection isolated from the full Candidate reader contract."""

from sqlalchemy.engine import Connection

from jobhunter.domain.evidence.models import FIELD_MODELS
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.domain.resume.models import ResumeVersion
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import (
    CandidateRepository,
    Json,
    checked,
    decoded,
)


class MaterialSources:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn
        self.candidate = CandidateRepository(conn)

    def read(self, resume_version_id: str) -> MaterialSource:
        row = self.candidate.row(
            "SELECT * FROM resume_versions WHERE resume_version_id=?", (resume_version_id,)
        )
        if row is None:
            raise Failure("NOT_FOUND")
        root = self.candidate.root("resume", row["resume_id"], required=True)
        profile = self.candidate.version("profile", row["profile_version_id"], required=True)
        row["header_presentation"] = decoded(row["header_presentation"])
        row["document_presentation"] = decoded(row["document_presentation"])
        sections: list[Json] = []
        sources: list[Json] = []
        for section in self.conn.exec_driver_sql(
            "SELECT position,kind FROM resume_sections WHERE resume_version_id=? ORDER BY position",
            (resume_version_id,),
        ).mappings():
            if section["position"] != len(sections):
                raise Failure("INTERNAL_ERROR")
            members: list[Json] = []
            for member in self.conn.exec_driver_sql(
                "SELECT * FROM resume_members WHERE resume_version_id=? AND section_position=? "
                "ORDER BY position",
                (resume_version_id, section["position"]),
            ).mappings():
                if member["position"] != len(members) or member["kind"] != section["kind"]:
                    raise Failure("INTERNAL_ERROR")
                fact = self.candidate.row(
                    "SELECT v.evidence_item_id,v.evidence_item_version_id,i.kind,v.fields "
                    "FROM evidence_item_versions v JOIN evidence_items i "
                    "ON i.evidence_item_id=v.evidence_item_id WHERE v.evidence_item_version_id=?",
                    (member["evidence_item_version_id"],),
                    required=True,
                )
                assert fact is not None
                if (
                    fact["evidence_item_id"] != member["evidence_item_id"]
                    or fact["kind"] != section["kind"]
                ):
                    raise Failure("INTERNAL_ERROR")
                fact["fields"] = checked(FIELD_MODELS[fact["kind"]], decoded(fact["fields"]))
                sources.append(fact)
                members.append(
                    {
                        "evidence_item_id": member["evidence_item_id"],
                        "evidence_item_version_id": member["evidence_item_version_id"],
                        "content": decoded(member["content"]),
                    }
                )
            sections.append({"kind": section["kind"], "members": members})
        row["sections"] = sections
        row = checked(ResumeVersion, row)
        if not root["created_at"] <= row["created_at"] <= root["updated_at"]:
            raise Failure("INTERNAL_ERROR")
        result = checked(
            MaterialSource,
            {"resume_version": row, "profile_version": profile, "evidence_sources": sources},
        )
        return MaterialSource.model_validate(result)
