"""Saved-authority HTTP projection; all mutations enter the Application coordinator."""

from typing import Annotated, Any

from fastapi import APIRouter, FastAPI, Path

from jobhunter.api.middleware.candidate_requests import CandidateRoute
from jobhunter.api.schemas.errors import ContractError
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.evidence import models as ev
from jobhunter.domain.profile import models as pr
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.values import UUID_PATTERN
from jobhunter.domain.workspace.selection import SetDefault
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json

Identity = Annotated[str, Path(pattern=UUID_PATTERN)]


def register_routes(app: FastAPI, authority: CandidateAuthority) -> None:
    errors: dict[int | str, dict[str, Any]] = {
        status: {"model": ContractError} for status in (400, 403, 404, 409, 413, 422, 500, 503)
    }
    router = APIRouter(
        prefix="/api/v1", route_class=CandidateRoute, responses=errors, tags=["Candidate authority"]
    )

    @router.get("/profile", response_model=pr.ProfilePair)
    def profile() -> Json:
        return authority.pair("profile")

    @router.get("/profile/versions/{profile_version_id}", response_model=pr.ProfileVersion)
    def profile_version(profile_version_id: Identity) -> Json:
        return authority.version("profile", profile_version_id)

    @router.post("/profile/save", response_model=pr.ProfileResult)
    def save_profile(command: pr.ProfileSave) -> Json:
        return authority.command("PROFILE_SAVE", command)

    @router.get("/evidence-items", response_model=ev.EvidenceList)
    def evidence_list() -> Json:
        return authority.list_evidence()

    @router.post("/evidence-items", response_model=ev.EvidenceResult)
    def create_evidence(command: ev.EvidenceCreate) -> Json:
        return authority.command("EVIDENCE_CREATE", command)

    @router.get(
        "/evidence-items/versions/{evidence_item_version_id}", response_model=ev.EvidenceExact
    )
    def evidence_version(evidence_item_version_id: Identity) -> Json:
        return authority.version("evidence_item", evidence_item_version_id)

    @router.get("/evidence-items/{evidence_item_id}", response_model=ev.EvidencePair)
    def evidence(evidence_item_id: Identity) -> Json:
        return authority.pair("evidence_item", evidence_item_id)

    @router.post("/evidence-items/{evidence_item_id}/save", response_model=ev.EvidenceResult)
    def save_evidence(evidence_item_id: Identity, command: ev.EvidenceUpdate) -> Json:
        return authority.command("EVIDENCE_UPDATE", command, evidence_item_id)

    @router.post("/evidence-items/{evidence_item_id}/retire", response_model=ev.EvidenceResult)
    def retire_evidence(evidence_item_id: Identity, command: ev.EvidenceRetire) -> Json:
        return authority.command("EVIDENCE_RETIRE", command, evidence_item_id)

    @router.get("/evidence-baselines/current", response_model=ev.Baseline)
    def current_baseline() -> Json:
        return authority.baseline()

    @router.get("/evidence-baselines/{evidence_baseline_snapshot_id}", response_model=ev.Baseline)
    def exact_baseline(evidence_baseline_snapshot_id: Identity) -> Json:
        return authority.baseline(evidence_baseline_snapshot_id)

    @router.get("/resumes", response_model=rs.ResumeList)
    def resumes() -> Json:
        return authority.list_resumes()

    @router.post("/resumes", response_model=rs.ResumeSelectionResult)
    def create_resume(command: rs.ResumeCreate) -> Json:
        return authority.command("RESUME_CREATE", command)

    @router.get("/resumes/versions/{resume_version_id}", response_model=rs.ResumeVersion)
    def resume_version(resume_version_id: Identity) -> Json:
        return authority.version("resume", resume_version_id)

    @router.get("/resumes/{resume_id}", response_model=rs.ResumePair)
    def resume(resume_id: Identity) -> Json:
        return authority.pair("resume", resume_id)

    @router.post("/resumes/{resume_id}/save", response_model=rs.ResumeResult)
    def save_resume(resume_id: Identity, command: rs.ResumeSave) -> Json:
        return authority.command("RESUME_SAVE", command, resume_id)

    @router.post("/resumes/{resume_id}/rename", response_model=rs.ResumeResult)
    def rename_resume(resume_id: Identity, command: rs.ResumeRename) -> Json:
        return authority.command("RESUME_RENAME", command, resume_id)

    @router.post("/resumes/{resume_id}/remove", response_model=rs.ResumeSelectionResult)
    def remove_resume(resume_id: Identity, command: rs.ResumeRemove) -> Json:
        return authority.command("RESUME_REMOVE", command, resume_id)

    @router.post("/workspace/default-resume/set", response_model=rs.SelectionResult)
    def set_default(command: SetDefault) -> Json:
        return authority.command("DEFAULT_RESUME_SET", command)

    app.include_router(router)
