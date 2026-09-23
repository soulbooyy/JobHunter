"""Coordinate the nine saved-authority commands in one short SQLite transaction."""

from collections.abc import Callable
from uuid import uuid4

from pydantic import BaseModel, TypeAdapter, ValidationError
from sqlalchemy.engine import Connection

from jobhunter.application.candidate.fingerprint import fingerprint
from jobhunter.application.manual_application_entries.service import utc_now
from jobhunter.domain.evidence import models as ev
from jobhunter.domain.profile import models as pr
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.candidate_values import FieldFailure, admit
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION, UuidV4
from jobhunter.domain.workspace.selection import SetDefault
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import (
    CandidateRepository,
    Json,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

COMMAND_MODELS: dict[str, type[BaseModel]] = {
    "PROFILE_SAVE": pr.ProfileSave,
    "EVIDENCE_CREATE": ev.EvidenceCreate,
    "EVIDENCE_UPDATE": ev.EvidenceUpdate,
    "EVIDENCE_RETIRE": ev.EvidenceRetire,
    "RESUME_CREATE": rs.ResumeCreate,
    "RESUME_SAVE": rs.ResumeSave,
    "RESUME_RENAME": rs.ResumeRename,
    "RESUME_REMOVE": rs.ResumeRemove,
    "DEFAULT_RESUME_SET": SetDefault,
}
PROFILE_KEYS = ("full_name", "phone_number", "email")
RESUME_KEYS = ("profile_version_id", "header_presentation", "sections", "document_presentation")


def identifier(value: str, field: str) -> str:
    try:
        return TypeAdapter[str](UuidV4).validate_python(value)
    except ValidationError:
        raise FieldFailure(field, "INVALID_FORMAT") from None


def revision(root: Json, expected: int) -> None:
    if root["revision"] != expected:
        raise Failure("REVISION_CONFLICT")


def advance(root: Json) -> Json:
    if root["revision"] == MAX_REVISION:
        raise Failure("REVISION_EXHAUSTED")
    return {**root, "revision": root["revision"] + 1}


def selected(data: Json, keys: tuple[str, ...]) -> Json:
    return {k: data[k] for k in keys}


class CandidateAuthority:
    def __init__(self, store: Store, *, clock: Callable[[], str] = utc_now) -> None:
        self.store, self.clock = store, clock

    def pair(self, name: str, identity: str | None = None) -> Json:
        if identity is not None:
            identifier(identity, name + "_id")
        return self.store.run(lambda conn: CandidateRepository(conn).pair(name, identity))

    def version(self, name: str, identity: str) -> Json:
        identifier(identity, name + "_version_id")

        def read(conn: Connection) -> Json:
            repo = CandidateRepository(conn)
            version = repo.version(name, identity)
            if name == "evidence_item":
                return {
                    "kind": repo.root(name, version[name + "_id"])["kind"],
                    "evidence_item_version": version,
                }
            return version

        return self.store.run(read)

    def baseline(self, identity: str | None = None) -> Json:
        if identity is not None:
            identifier(identity, "evidence_baseline_snapshot_id")
        return self.store.run(lambda conn: CandidateRepository(conn).baseline(identity))

    def list_evidence(self) -> Json:
        def read(conn: Connection) -> Json:
            repo = CandidateRepository(conn)
            entries: list[Json] = []
            for identity in conn.exec_driver_sql(
                "SELECT evidence_item_id FROM evidence_items WHERE status='ACTIVE' ORDER BY"
                " created_at,evidence_item_id"
            ).scalars():
                pair = repo.pair("evidence_item", identity)
                entries.append(
                    {
                        "evidence_item": pair["evidence_item"],
                        "current_evidence_item_version_id": pair["evidence_item_version"][
                            "evidence_item_version_id"
                        ],
                        "fields": pair["evidence_item_version"]["fields"],
                    }
                )
            return {"evidence_items": entries}

        return self.store.run(read)

    def list_resumes(self) -> Json:
        def read(conn: Connection) -> Json:
            repo = CandidateRepository(conn)
            return {
                "resumes": [
                    repo.pair("resume", identity)["resume"]
                    for identity in conn.exec_driver_sql(
                        "SELECT resume_id FROM resumes WHERE status='ACTIVE' ORDER BY "
                        "created_at,resume_id"
                    ).scalars()
                ],
                "default_resume_selection": repo.selection(),
            }

        return self.store.run(read)

    def command(
        self, command_type: str, command: BaseModel | Json, target: str | None = None
    ) -> Json:
        # Re-admit application callers, including model_construct and mutated collections.
        data = admit(
            COMMAND_MODELS[command_type],
            command.model_dump() if isinstance(command, BaseModel) else command,
        ).model_dump(mode="json")
        if target is not None:
            identifier(
                target, "evidence_item_id" if command_type.startswith("EVIDENCE") else "resume_id"
            )
        if command_type in ("EVIDENCE_CREATE", "EVIDENCE_UPDATE"):
            kind = data.get("kind")
            if command_type == "EVIDENCE_UPDATE":
                # The sole pre-receipt target read selects immutable kind, never mutable admission.
                kind = self.store.run(
                    lambda conn: CandidateRepository(conn).root("evidence_item", target)["kind"]
                )
            assert isinstance(kind, str)
            data["fields"] = admit(ev.FIELD_MODELS[kind], data["fields"], "fields").model_dump(
                mode="json"
            )
        digest = fingerprint(command_type, target, data)

        def execute(conn: Connection) -> Json:
            repo = CandidateRepository(conn)
            replay = repo.receipt(data["request_id"], command_type, digest)
            if replay is not None:
                return replay
            if command_type == "PROFILE_SAVE":
                result = self.save_profile(repo, data)
            elif command_type.startswith("EVIDENCE_"):
                result = self.evidence(repo, command_type, target, data)
            elif command_type == "DEFAULT_RESUME_SET":
                result = self.set_default(repo, data)
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

    def save_profile(self, repo: CandidateRepository, data: Json) -> Json:
        pair = repo.pair("profile")
        root, version = pair["profile"], pair["profile_version"]
        revision(root, data["revision"])
        content = selected(data, PROFILE_KEYS)
        if content == selected(version, PROFILE_KEYS):
            return {**pair, "outcome": "UNCHANGED"}
        root = self.changed(root, self.clock())
        root["current_profile_version_id"] = str(uuid4())
        version = {
            "profile_id": root["profile_id"],
            "profile_version_id": root["current_profile_version_id"],
            "schema_version": 1,
            "created_at": root["updated_at"],
            **content,
        }
        repo.publish("profile", root, version)
        return {"profile": root, "profile_version": version, "outcome": "UPDATED"}

    def evidence(
        self, repo: CandidateRepository, command: str, target: str | None, data: Json
    ) -> Json:
        first = command == "EVIDENCE_CREATE"
        pair = None if first else repo.pair("evidence_item", target)
        if pair is not None:
            revision(pair["evidence_item"], data["revision"])
        baseline = repo.baseline()
        baseline_id = baseline["evidence_baseline_snapshot_id"]
        now = max(self.clock(), baseline["created_at"])
        if first:
            if repo.count("evidence_item") >= 1000:
                raise Failure("CAPACITY_EXCEEDED")
            root: Json = {
                "evidence_item_id": str(uuid4()),
                "kind": data["kind"],
                "status": "ACTIVE",
                "current_evidence_item_version_id": str(uuid4()),
                "revision": 1,
                "created_at": now,
                "updated_at": now,
            }
            outcome = "CREATED"
        else:
            assert pair is not None
            root, old = pair["evidence_item"], pair["evidence_item_version"]
            if command == "EVIDENCE_UPDATE" and root["status"] != "ACTIVE":
                raise Failure("INVALID_STATE")
            if (command == "EVIDENCE_RETIRE" and root["status"] == "RETIRED") or (
                command == "EVIDENCE_UPDATE"
                and selected(old, ("fields", "content")) == selected(data, ("fields", "content"))
            ):
                return {
                    **pair,
                    "outcome": "UNCHANGED",
                    "evidence_baseline_snapshot_id": baseline_id,
                }
            root = self.changed(root, now)
            now = root["updated_at"]
            outcome = "RETIRED" if command == "EVIDENCE_RETIRE" else "UPDATED"
            if command == "EVIDENCE_RETIRE":
                root["status"] = "RETIRED"
            else:
                root["current_evidence_item_version_id"] = str(uuid4())
        if command == "EVIDENCE_RETIRE":
            assert pair is not None
            version = pair["evidence_item_version"]
            repo.publish("evidence_item", root, None)
        else:
            version = {
                "evidence_item_id": root["evidence_item_id"],
                "evidence_item_version_id": root["current_evidence_item_version_id"],
                "schema_version": 1,
                "created_at": now,
                **selected(data, ("fields", "content")),
            }
            repo.publish("evidence_item", root, version, first=first)
        self.store.fault("candidate_before_baseline")
        baseline_id = str(uuid4())
        repo.publish_baseline(baseline_id, now)
        return {
            "evidence_item": root,
            "evidence_item_version": version,
            "evidence_baseline_snapshot_id": baseline_id,
            "outcome": outcome,
        }

    def sources(self, repo: CandidateRepository, data: Json, old: Json | None) -> None:
        try:
            profile = repo.version("profile", data["profile_version_id"])
        except Failure as exc:
            if exc.code == "NOT_FOUND":
                raise FieldFailure("profile_version_id", "INVALID_REFERENCE") from None
            raise
        if old is None or old["profile_version_id"] != profile["profile_version_id"]:
            if repo.root("profile")["current_profile_version_id"] != profile["profile_version_id"]:
                raise Failure("SOURCE_CONFLICT")
        previous: set[tuple[str, str]] = (
            set()
            if old is None
            else {
                (m["evidence_item_id"], m["evidence_item_version_id"])
                for s in old["sections"]
                for m in s["members"]
            }
        )
        for s_index, section in enumerate(data["sections"]):
            for m_index, member in enumerate(section["members"]):
                path = f"sections[{s_index}].members[{m_index}]"
                try:
                    root = repo.root("evidence_item", member["evidence_item_id"])
                except Failure as exc:
                    if exc.code == "NOT_FOUND":
                        raise FieldFailure(
                            path + ".evidence_item_id", "INVALID_REFERENCE"
                        ) from None
                    raise
                try:
                    version = repo.version("evidence_item", member["evidence_item_version_id"])
                except Failure as exc:
                    if exc.code == "NOT_FOUND":
                        raise FieldFailure(
                            path + ".evidence_item_version_id", "INVALID_REFERENCE"
                        ) from None
                    raise
                if version["evidence_item_id"] != root["evidence_item_id"]:
                    raise FieldFailure(path + ".evidence_item_version_id", "INVALID_REFERENCE")
                if section["kind"] != root["kind"]:
                    raise FieldFailure(f"sections[{s_index}].kind", "INVALID_REFERENCE")
                if (
                    member["evidence_item_id"],
                    member["evidence_item_version_id"],
                ) not in previous and (
                    root["status"] != "ACTIVE"
                    or root["current_evidence_item_version_id"]
                    != member["evidence_item_version_id"]
                ):
                    raise Failure("SOURCE_CONFLICT")

    def resume(
        self, repo: CandidateRepository, command: str, target: str | None, data: Json
    ) -> Json:
        selection: Json = {}
        first = command == "RESUME_CREATE"
        pair = None if first else repo.pair("resume", target)
        if pair is not None:
            revision(pair["resume"], data["revision"])
        if command == "RESUME_REMOVE":
            assert pair is not None
            return self.remove(repo, pair, data)
        if pair is not None and pair["resume"]["status"] != "ACTIVE":
            raise Failure("INVALID_STATE")
        if command != "RESUME_RENAME":
            self.sources(repo, data, None if pair is None else pair["resume_version"])
        if pair is not None:
            equal = (
                pair["resume"]["resume_name"] == data["resume_name"]
                if command == "RESUME_RENAME"
                else selected(pair["resume_version"], RESUME_KEYS) == selected(data, RESUME_KEYS)
            )
            if equal:
                return {**pair, "outcome": "UNCHANGED"}
        if first:
            if repo.count("resume") >= 100:
                raise Failure("CAPACITY_EXCEEDED")
            selection = repo.selection()
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
        else:
            assert pair is not None
            root = self.changed(pair["resume"], self.clock())
            if command == "RESUME_RENAME":
                root["resume_name"] = data["resume_name"]
                repo.publish("resume", root, None)
                return {
                    "resume": root,
                    "resume_version": pair["resume_version"],
                    "outcome": "UPDATED",
                }
            root["current_resume_version_id"] = str(uuid4())
        version = {
            "resume_id": root["resume_id"],
            "resume_version_id": root["current_resume_version_id"],
            "schema_version": 1,
            "created_at": root["updated_at"],
            **selected(data, RESUME_KEYS),
        }
        repo.publish("resume", root, version, first=first)
        result = {
            "resume": root,
            "resume_version": version,
            "outcome": "CREATED" if first else "UPDATED",
        }
        if first:
            if selection["default_resume_id"] is None:
                selection = {**advance(selection), "default_resume_id": root["resume_id"]}
                repo.set_selection(selection)
            result["default_resume_selection"] = selection
        return result

    def active_replacement(self, repo: CandidateRepository, identity: str, field: str) -> Json:
        try:
            root = repo.pair("resume", identity)["resume"]
        except Failure as exc:
            if exc.code == "NOT_FOUND":
                raise FieldFailure(field, "INVALID_REFERENCE") from None
            raise
        if root["status"] != "ACTIVE":
            raise Failure("INVALID_STATE")
        return root

    def set_default(self, repo: CandidateRepository, data: Json) -> Json:
        selection = repo.selection()
        revision(selection, data["revision"])
        self.active_replacement(repo, data["default_resume_id"], "default_resume_id")
        if selection["default_resume_id"] == data["default_resume_id"]:
            return {"default_resume_selection": selection, "outcome": "UNCHANGED"}
        selection = {**advance(selection), "default_resume_id": data["default_resume_id"]}
        repo.set_selection(selection)
        return {"default_resume_selection": selection, "outcome": "UPDATED"}

    def remove(self, repo: CandidateRepository, pair: Json, data: Json) -> Json:
        root = pair["resume"]
        selection = repo.selection()
        if root["status"] == "REMOVED":
            return {**pair, "default_resume_selection": selection, "outcome": "UNCHANGED"}
        revision(selection, data["default_resume_selection"]["revision"])
        if repo.count("resume") == 1:
            raise Failure("LAST_RESUME_REQUIRED")
        replacement = data["replacement_resume_id"]
        if selection["default_resume_id"] == root["resume_id"]:
            if replacement is None or replacement == root["resume_id"]:
                raise FieldFailure("replacement_resume_id", "INVALID_REFERENCE")
            self.active_replacement(repo, replacement, "replacement_resume_id")
            selection = {**advance(selection), "default_resume_id": replacement}
        elif replacement is not None:
            raise FieldFailure("replacement_resume_id", "INVALID_REFERENCE")
        root = {**self.changed(root, self.clock()), "status": "REMOVED"}
        repo.publish("resume", root, None)
        repo.set_selection(selection)
        return {
            "resume": root,
            "resume_version": pair["resume_version"],
            "default_resume_selection": selection,
            "outcome": "REMOVED",
        }
