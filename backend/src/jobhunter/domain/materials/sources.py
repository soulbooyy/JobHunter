"""Transient exact rendering inputs; no Evidence expression or new source identity."""

from jobhunter.domain.evidence.models import Fields, Kind
from jobhunter.domain.profile.models import ProfileVersion
from jobhunter.domain.resume.models import ResumeVersion
from jobhunter.domain.shared.values import DTO, UuidV4


class EvidenceSource(DTO):
    evidence_item_id: UuidV4
    evidence_item_version_id: UuidV4
    kind: Kind
    fields: Fields


class MaterialSource(DTO):
    resume_version: ResumeVersion
    profile_version: ProfileVersion
    evidence_sources: list[EvidenceSource]
