"""Coordinate six independent-Resume/default/portrait commands in short transactions."""

from collections.abc import Callable
from uuid import uuid4

from pydantic import BaseModel, TypeAdapter, ValidationError
from sqlalchemy.engine import Connection

from jobhunter.application.candidate.fingerprint import fingerprint
from jobhunter.application.manual_application_entries.service import utc_now
from jobhunter.domain.profile import models as pr
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.candidate_values import FieldFailure, admit
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION, UuidV4
from jobhunter.domain.workspace.selection import SetDefault
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import (
    CandidateRepository,
    Json,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

COMMAND_MODELS: dict[str, type[BaseModel]] = {
    "RESUME_CREATE": rs.ResumeCreate,
    "RESUME_SAVE": rs.ResumeSave,
    "RESUME_RENAME": rs.ResumeRename,
    "RESUME_REMOVE": rs.ResumeRemove,
    "DEFAULT_RESUME_SET": SetDefault,
    "PORTRAIT_REFRESH": pr.PortraitRefresh,
}
CONTENT_KEYS = ("contacts", "header_presentation", "sections", "document_presentation")


def identifier(value: str, field: str) -> str:
    try:
        return TypeAdapter[str](UuidV4).validate_python(value)
    except ValidationError:
        raise FieldFailure(field, "INVALID_FORMAT") from None


def revision(value: Json, expected: int) -> None:
    if value["revision"] != expected:
        raise Failure("REVISION_CONFLICT")


def advance(value: Json) -> Json:
    if value["revision"] == MAX_REVISION:
        raise Failure("REVISION_EXHAUSTED")
    return {**value, "revision": value["revision"] + 1}


def selected(value: Json, keys: tuple[str, ...]) -> Json:
    return {key: value[key] for key in keys}


class CandidateAuthority:
    def __init__(self, store: Store, *, clock: Callable[[], str] = utc_now) -> None:
        self.store, self.clock = store, clock

    def pair(self, identity: str) -> Json:
        identifier(identity, "resume_id")
        return self.store.run(lambda conn: CandidateRepository(conn).pair(identity))

    def version(self, identity: str) -> Json:
        identifier(identity, "resume_version_id")
        return self.store.run(lambda conn: CandidateRepository(conn).version(identity))

    def list_resumes(self) -> Json:
        return self.store.run(lambda conn: CandidateRepository(conn).list_resumes())

    def portrait(self) -> Json:
        return self.store.run(lambda conn: CandidateRepository(conn).portrait_read())

    def command(
        self, command_type: str, command: BaseModel | Json, target: str | None = None
    ) -> Json:
        data = admit(
            COMMAND_MODELS[command_type],
            command.model_dump() if isinstance(command, BaseModel) else command,
        ).model_dump(mode="json")
        if target is not None:
            identifier(target, "resume_id")
        digest = fingerprint(command_type, target, data)

        def execute(conn: Connection) -> Json:
            repo = CandidateRepository(conn)
            replay = repo.receipt(data["request_id"], command_type, digest)
            if replay is not None:
                return replay
            if command_type == "DEFAULT_RESUME_SET":
                result = self.set_default(repo, data)
            elif command_type == "PORTRAIT_REFRESH":
                result = self.refresh(repo, data)
            else:
                result = self.resume(repo, command_type, target, data)
            result["request_id"] = data["request_id"]
            self.store.fault("candidate_after_publication")
            repo.record(command_type, digest, result)
            self.store.fault("candidate_after_receipt")
            return result

        return self.store.run(execute, write=True)

    def changed(self, root: Json, now: str) -> Json:
        return {**advance(root), "updated_at": max(now, root["updated_at"])}

    def active(self, repo: CandidateRepository, identity: str, field: str) -> Json:
        try:
            root = repo.root(identity)
        except Failure as exc:
            if exc.code == "NOT_FOUND":
                raise FieldFailure(field, "INVALID_REFERENCE") from None
            raise
        if root["status"] != "ACTIVE":
            raise Failure("INVALID_STATE")
        return root

    def resume(
        self, repo: CandidateRepository, command: str, target: str | None, data: Json
    ) -> Json:
        first = command == "RESUME_CREATE"
        if first:
            if repo.count() >= 100:
                raise Failure("CAPACITY_EXCEEDED")
            now = self.clock()
            root: Json = {
                "resume_id": str(uuid4()),
                "resume_name": data["resume_name"],
                "status": "ACTIVE",
                "current_resume_version_id": str(uuid4()),
                "revision": 1,
                "created_at": now,
                "updated_at": now,
            }
            old_version = None
        else:
            assert target is not None
            pair = repo.pair(target)
            root, old_version = pair["resume"], pair["resume_version"]
            revision(root, data["revision"])
            if command == "RESUME_REMOVE":
                return self.remove(repo, pair, data)
            if root["status"] != "ACTIVE":
                raise Failure("INVALID_STATE")
            if command == "RESUME_RENAME":
                if root["resume_name"] == data["resume_name"]:
                    return {**pair, "outcome": "UNCHANGED"}
                root = {**self.changed(root, self.clock()), "resume_name": data["resume_name"]}
                repo.publish(root, None)
                return {"resume": root, "resume_version": old_version, "outcome": "UPDATED"}

        content = selected(data, CONTENT_KEYS)
        if old_version is not None and content == selected(old_version, CONTENT_KEYS):
            return {"resume": root, "resume_version": old_version, "outcome": "UNCHANGED"}
        if not first:
            root = self.changed(root, self.clock())
            root["current_resume_version_id"] = str(uuid4())
        version = {
            "resume_version_id": root["current_resume_version_id"],
            "resume_id": root["resume_id"],
            "schema_version": 2,
            **content,
            "created_at": root["updated_at"],
        }
        repo.publish(root, version, first=first)
        selection = repo.selection()
        result: Json = {
            "resume": root,
            "resume_version": version,
            "outcome": "CREATED" if first else "UPDATED",
        }
        if first:
            if selection["default_resume_id"] is None:
                selection = {**advance(selection), "default_resume_id": root["resume_id"]}
                repo.set_selection(selection)
                version_id = version["resume_version_id"]
                assert isinstance(version_id, str)
                repo.set_portrait_source(version_id, root["updated_at"])
            result["default_resume_selection"] = selection
        elif selection["default_resume_id"] == root["resume_id"]:
            version_id = version["resume_version_id"]
            assert isinstance(version_id, str)
            repo.set_portrait_source(version_id, root["updated_at"])
        return result

    def remove(self, repo: CandidateRepository, pair: Json, data: Json) -> Json:
        root = pair["resume"]
        selection = repo.selection()
        if root["status"] == "REMOVED":
            return {**pair, "default_resume_selection": selection, "outcome": "UNCHANGED"}
        revision(selection, data["default_resume_selection"]["revision"])
        replacement = data["replacement_resume_id"]
        default = selection["default_resume_id"] == root["resume_id"]
        source: str | None = None
        if default:
            remaining = repo.count() - 1
            if remaining:
                if replacement is None or replacement == root["resume_id"]:
                    raise FieldFailure("replacement_resume_id", "INVALID_REFERENCE")
                replacement_root = self.active(repo, replacement, "replacement_resume_id")
                candidate_source = replacement_root["current_resume_version_id"]
                assert isinstance(candidate_source, str)
                source = candidate_source
            else:
                if replacement is not None:
                    raise FieldFailure("replacement_resume_id", "INVALID_REFERENCE")
                source = None
            selection = {**advance(selection), "default_resume_id": replacement}
        elif replacement is not None:
            raise FieldFailure("replacement_resume_id", "INVALID_REFERENCE")
        root = {**self.changed(root, self.clock()), "status": "REMOVED"}
        repo.publish(root, None)
        if default:
            repo.set_selection(selection)
            repo.set_portrait_source(source, root["updated_at"])
        return {
            "resume": root,
            "resume_version": pair["resume_version"],
            "default_resume_selection": selection,
            "outcome": "REMOVED",
        }

    def set_default(self, repo: CandidateRepository, data: Json) -> Json:
        selection = repo.selection()
        revision(selection, data["revision"])
        root = self.active(repo, data["default_resume_id"], "default_resume_id")
        if selection["default_resume_id"] == root["resume_id"]:
            return {"default_resume_selection": selection, "outcome": "UNCHANGED"}
        selection = {**advance(selection), "default_resume_id": root["resume_id"]}
        repo.set_selection(selection)
        repo.set_portrait_source(root["current_resume_version_id"], self.clock())
        return {"default_resume_selection": selection, "outcome": "UPDATED"}

    def refresh(self, repo: CandidateRepository, data: Json) -> Json:
        selection = repo.selection()
        revision(selection, data["default_resume_selection"]["revision"])
        if selection["default_resume_id"] is None:
            raise Failure("INVALID_STATE")
        root = self.active(repo, selection["default_resume_id"], "default_resume_id")
        if root["current_resume_version_id"] != data["source_resume_version_id"]:
            raise Failure("SOURCE_CONFLICT")
        current = repo.portrait_read()["state"]
        if current["status"] == "EMPTY_SOURCE":
            raise Failure("INVALID_STATE")
        if current["source_resume_version_id"] == data["source_resume_version_id"] and current[
            "status"
        ] in ("QUEUED", "RUNNING"):
            build = repo.portrait_build(current["build_id"])
            if build["trigger_mode"] == "FULL":
                return {"state": current, "outcome": "UNCHANGED"}
        state = repo.set_portrait_source(
            data["source_resume_version_id"], self.clock(), trigger_mode="FULL"
        )
        return {"state": state, "outcome": "UPDATED"}
