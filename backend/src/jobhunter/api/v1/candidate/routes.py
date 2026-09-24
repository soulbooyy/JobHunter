"""Saved-authority HTTP projection; all mutations enter the Application coordinator."""

from typing import Annotated, Any

from fastapi import APIRouter, FastAPI, Path

from jobhunter.api.middleware.candidate_requests import CandidateRoute
from jobhunter.api.schemas.errors import ContractError
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.profile import models as pr
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.values import UUID_PATTERN
from jobhunter.domain.workspace.selection import SetDefault
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import Json

Identity = Annotated[str, Path(pattern=UUID_PATTERN)]


def register_routes(app: FastAPI, authority: CandidateAuthority) -> None:
    errors: dict[int | str, dict[str, Any]] = {
        status: {"model": ContractError} for status in (400, 403, 404, 409, 413, 422, 500, 503)
    }
    router = APIRouter(
        prefix="/api/v1", route_class=CandidateRoute, responses=errors, tags=["Candidate authority"]
    )

    @router.get("/resumes", response_model=rs.ResumeList)
    def resumes() -> Json:
        return authority.list_resumes()

    @router.post("/resumes", response_model=rs.ResumeSelectionResult)
    def create_resume(command: rs.ResumeCreate) -> Json:
        return authority.command("RESUME_CREATE", command)

    @router.get("/resumes/versions/{resume_version_id}", response_model=rs.ResumeVersion)
    def resume_version(resume_version_id: Identity) -> Json:
        return authority.version(resume_version_id)

    @router.get("/resumes/{resume_id}", response_model=rs.ResumePair)
    def resume(resume_id: Identity) -> Json:
        return authority.pair(resume_id)

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

    @router.get("/workspace/portrait", response_model=pr.PortraitRead)
    def portrait() -> Json:
        return authority.portrait()

    @router.post("/workspace/portrait/refresh", response_model=pr.PortraitRefreshResult)
    def refresh_portrait(command: pr.PortraitRefresh) -> Json:
        return authority.command("PORTRAIT_REFRESH", command)

    app.include_router(router)
