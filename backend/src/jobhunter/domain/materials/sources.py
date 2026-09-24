"""Transient exact schema-2 Resume rendering input."""

from jobhunter.domain.resume.models import ResumeVersion
from jobhunter.domain.shared.values import DTO


class MaterialSource(DTO):
    resume_version: ResumeVersion
