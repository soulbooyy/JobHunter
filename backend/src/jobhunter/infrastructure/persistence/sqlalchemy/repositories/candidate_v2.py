"""Independent Resume persistence and deterministic portrait-source preparation."""

# ruff: noqa: E501 -- SQL statements stay readable as complete owned operations.

import json
from decimal import Decimal, DecimalException
from typing import Any, cast
from uuid import uuid4

from pydantic import BaseModel, ValidationError
from sqlalchemy.engine import Connection

from jobhunter.domain.evidence.models import CandidateEvidenceProjection
from jobhunter.domain.profile.incremental import (
    DerivationPlan,
    assemble_profile,
    make_plan,
)
from jobhunter.domain.profile.models import (
    CurrentPortraitState,
    Portrait,
    PortraitRead,
    PortraitRefreshResult,
)
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.candidate_values import FieldFailure
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION
from jobhunter.domain.workspace.selection import DefaultSelection

Json = dict[str, Any]
EXTRACTION_KEY = "resume.v1"
RESULT_MODELS: dict[str, type[BaseModel]] = {
    "RESUME_CREATE": rs.ResumeSelectionResult,
    "RESUME_REMOVE": rs.ResumeSelectionResult,
    "RESUME_SAVE": rs.ResumeResult,
    "RESUME_RENAME": rs.ResumeResult,
    "DEFAULT_RESUME_SET": rs.SelectionResult,
    "PORTRAIT_REFRESH": PortraitRefreshResult,
}
RESULT_OUTCOMES = {
    "RESUME_CREATE": {"CREATED"},
    "RESUME_SAVE": {"UPDATED", "UNCHANGED"},
    "RESUME_RENAME": {"UPDATED", "UNCHANGED"},
    "RESUME_REMOVE": {"REMOVED", "UNCHANGED"},
    "DEFAULT_RESUME_SET": {"UPDATED", "UNCHANGED"},
    "PORTRAIT_REFRESH": {"UPDATED", "UNCHANGED"},
}


def checked(model: type[BaseModel], value: Json) -> Json:
    try:
        canonical = model.model_validate(value).model_dump(mode="json")
        if canonical != value:
            raise Failure("INTERNAL_ERROR")
        return canonical
    except (ValidationError, ValueError, TypeError):
        raise Failure("INTERNAL_ERROR") from None


def decoded(value: Any) -> Any:
    try:
        return json.loads(value, parse_float=Decimal)
    except (ValueError, TypeError, DecimalException):
        raise Failure("INTERNAL_ERROR") from None


def encoded(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


class CandidateRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def row(
        self, sql: str, args: tuple[object, ...] = (), *, required: bool = False
    ) -> Json | None:
        row = self.conn.exec_driver_sql(sql, args).mappings().first()
        if row is None:
            if required:
                raise Failure("INTERNAL_ERROR")
            return None
        return dict(row)

    def insert(self, table: str, data: Json) -> None:
        self.conn.exec_driver_sql(
            f"INSERT INTO {table} ({','.join(data)}) VALUES ({','.join('?' for _ in data)})",
            tuple(data.values()),
        )

    def root(self, identity: str, *, required: bool = False) -> Json:
        row = self.row("SELECT * FROM resumes WHERE resume_id=?", (identity,), required=required)
        if row is None:
            raise Failure("NOT_FOUND")
        return checked(rs.Resume, row)

    def version(self, identity: str, *, required: bool = False) -> Json:
        row = self.row(
            "SELECT * FROM resume_versions WHERE resume_version_id=?",
            (identity,),
            required=required,
        )
        if row is None:
            raise Failure("NOT_FOUND")
        row["contacts"] = decoded(row["contacts"])
        row["header_presentation"] = decoded(row["header_presentation"])
        row["document_presentation"] = decoded(row["document_presentation"])
        sections: list[Json] = []
        for section in self.conn.exec_driver_sql(
            "SELECT position,kind FROM resume_sections WHERE resume_version_id=? ORDER BY position",
            (identity,),
        ).mappings():
            if section["position"] != len(sections):
                raise Failure("INTERNAL_ERROR")
            members: list[Json] = []
            for member in self.conn.exec_driver_sql(
                "SELECT * FROM resume_entries WHERE resume_version_id=? AND section_position=? ORDER BY position",
                (identity, section["position"]),
            ).mappings():
                if member["position"] != len(members) or member["kind"] != section["kind"]:
                    raise Failure("INTERNAL_ERROR")
                members.append(
                    {
                        "entry_id": member["entry_id"],
                        "fields": decoded(member["fields"]),
                        "content": decoded(member["content"]),
                    }
                )
            sections.append({"kind": section["kind"], "members": members})
        row["sections"] = sections
        result = checked(rs.ResumeVersion, row)
        root = self.root(result["resume_id"], required=True)
        if result["created_at"] < root["created_at"] or result["created_at"] > root["updated_at"]:
            raise Failure("INTERNAL_ERROR")
        self._check_block_index(result)
        return result

    def _check_block_index(self, version: Json) -> None:
        expected: list[tuple[str, str, int]] = []
        for section in version["sections"]:
            for entry in section["members"]:
                position = 0
                for block in entry["content"]:
                    items = [block] if block["type"] == "PARAGRAPH" else block["items"]
                    for item in items:
                        expected.append((entry["entry_id"], item["block_id"], position))
                        position += 1
        actual = [
            tuple(row)
            for row in self.conn.exec_driver_sql(
                "SELECT entry_id,block_id,position FROM resume_blocks WHERE resume_version_id=? ORDER BY entry_id,position",
                (version["resume_version_id"],),
            ).all()
        ]
        if sorted(expected) != sorted(actual):
            raise Failure("INTERNAL_ERROR")

    def pair(self, identity: str) -> Json:
        root = self.root(identity)
        version = self.version(root["current_resume_version_id"], required=True)
        if version["resume_id"] != root["resume_id"]:
            raise Failure("INTERNAL_ERROR")
        return {"resume": root, "resume_version": version}

    def list_resumes(self) -> Json:
        roots = [
            self.root(identity, required=True)
            for identity in self.conn.exec_driver_sql(
                "SELECT resume_id FROM resumes WHERE status='ACTIVE' ORDER BY created_at,resume_id"
            ).scalars()
        ]
        return {"resumes": roots, "default_resume_selection": self.selection()}

    def selection(self) -> Json:
        row = self.row(
            "SELECT default_resume_id,revision FROM default_resume_selection WHERE singleton_key=1",
            required=True,
        )
        assert row is not None
        selection = checked(DefaultSelection, row)
        if selection["default_resume_id"] is not None:
            if self.root(selection["default_resume_id"], required=True)["status"] != "ACTIVE":
                raise Failure("INTERNAL_ERROR")
        return selection

    def set_selection(self, selection: Json) -> None:
        self.conn.exec_driver_sql(
            "UPDATE default_resume_selection SET default_resume_id=?,revision=? WHERE singleton_key=1",
            (selection["default_resume_id"], selection["revision"]),
        )

    def count(self) -> int:
        return int(
            self.conn.exec_driver_sql(
                "SELECT count(*) FROM resumes WHERE status='ACTIVE'"
            ).scalar_one()
        )

    def claim_logical_ids(self, resume_id: str, version: Json) -> None:
        entries: list[tuple[str, str]] = []
        blocks: list[tuple[str, str]] = []
        for section_position, section in enumerate(version["sections"]):
            for entry_position, entry in enumerate(section["members"]):
                prefix = f"sections[{section_position}].members[{entry_position}]"
                entries.append((entry["entry_id"], prefix + ".entry_id"))
                for block_position, block in enumerate(entry["content"]):
                    if block["type"] == "PARAGRAPH":
                        blocks.append(
                            (block["block_id"], prefix + f".content[{block_position}].block_id")
                        )
                    else:
                        blocks.extend(
                            (
                                item["block_id"],
                                prefix
                                + f".content[{block_position}].items[{item_position}].block_id",
                            )
                            for item_position, item in enumerate(block["items"])
                        )
        for table, column, values in (
            ("resume_entry_owners", "entry_id", entries),
            ("resume_block_owners", "block_id", blocks),
        ):
            for value, field in values:
                owner = self.conn.exec_driver_sql(
                    f"SELECT resume_id FROM {table} WHERE {column}=?", (value,)
                ).scalar()
                if owner is not None and owner != resume_id:
                    raise FieldFailure(field, "INVALID_REFERENCE")
                if owner is None:
                    self.insert(table, {column: value, "resume_id": resume_id})

    def publish(self, root: Json, version: Json | None, *, first: bool = False) -> None:
        if first:
            self.insert("resumes", root)
        else:
            values = {key: value for key, value in root.items() if key != "resume_id"}
            self.conn.exec_driver_sql(
                f"UPDATE resumes SET {','.join(key + '=?' for key in values)} WHERE resume_id=?",
                (*values.values(), root["resume_id"]),
            )
        if version is None:
            return
        self.claim_logical_ids(root["resume_id"], version)
        data = dict(version)
        sections = cast(list[Json], data.pop("sections"))
        for name in ("contacts", "header_presentation", "document_presentation"):
            data[name] = encoded(data[name])
        self.insert("resume_versions", data)
        for section_position, section in enumerate(sections):
            self.insert(
                "resume_sections",
                {
                    "resume_version_id": version["resume_version_id"],
                    "position": section_position,
                    "kind": section["kind"],
                },
            )
            for position, entry in enumerate(section["members"]):
                self.insert(
                    "resume_entries",
                    {
                        "resume_version_id": version["resume_version_id"],
                        "resume_id": root["resume_id"],
                        "section_position": section_position,
                        "position": position,
                        "kind": section["kind"],
                        "entry_id": entry["entry_id"],
                        "fields": encoded(entry["fields"]),
                        "content": encoded(entry["content"]),
                    },
                )
                block_position = 0
                for block in entry["content"]:
                    items = [block] if block["type"] == "PARAGRAPH" else block["items"]
                    for item in items:
                        self.insert(
                            "resume_blocks",
                            {
                                "resume_version_id": version["resume_version_id"],
                                "resume_id": root["resume_id"],
                                "entry_id": entry["entry_id"],
                                "position": block_position,
                                "block_id": item["block_id"],
                            },
                        )
                        block_position += 1

    def _derive_evidence_projection(self, resume_version_id: str) -> Json:
        version = self.version(resume_version_id)
        entries: list[Json] = []
        blocks: list[Json] = []
        for section in version["sections"]:
            for entry in section["members"]:
                entries.append(
                    {
                        "evidence_id": "entry/" + entry["entry_id"],
                        "entry_id": entry["entry_id"],
                        "kind": section["kind"],
                        "fields": entry["fields"],
                        "content": entry["content"],
                    }
                )
                for block in entry["content"]:
                    items = [block] if block["type"] == "PARAGRAPH" else block["items"]
                    for item in items:
                        blocks.append(
                            {
                                "evidence_id": f"block/{entry['entry_id']}/{item['block_id']}",
                                "entry_id": entry["entry_id"],
                                "block_id": item["block_id"],
                                "text": "".join(run["text"] for run in item["runs"]),
                            }
                        )
        return CandidateEvidenceProjection.model_validate(
            {
                "schema_version": 1,
                "resume_version_id": resume_version_id,
                "extraction_key": EXTRACTION_KEY,
                "entries": entries,
                "blocks": blocks,
            }
        ).model_dump(mode="json")

    def evidence_projection(self, resume_version_id: str) -> Json:
        stored = self.row(
            "SELECT projection FROM candidate_evidence_projections WHERE resume_version_id=?",
            (resume_version_id,),
        )
        if stored is None:
            raise Failure("INTERNAL_ERROR")
        projection = checked(CandidateEvidenceProjection, decoded(stored["projection"]))
        if projection != self._derive_evidence_projection(resume_version_id):
            raise Failure("INTERNAL_ERROR")
        return projection

    def ensure_evidence_projection(self, resume_version_id: str) -> Json:
        stored = self.row(
            "SELECT projection FROM candidate_evidence_projections WHERE resume_version_id=?",
            (resume_version_id,),
        )
        if stored is not None:
            return self.evidence_projection(resume_version_id)
        projection = self._derive_evidence_projection(resume_version_id)
        self.insert(
            "candidate_evidence_projections",
            {
                "resume_version_id": resume_version_id,
                "extraction_key": EXTRACTION_KEY,
                "projection": encoded(projection),
            },
        )
        return projection

    def set_portrait_source(
        self,
        source_version_id: str | None,
        now: str,
        *,
        trigger_mode: str = "AUTOMATIC",
    ) -> Json:
        selection = self.selection()
        current = self.portrait_read()["state"]
        if current["build_id"] is not None and current["status"] in ("QUEUED", "RUNNING"):
            self.conn.exec_driver_sql(
                "UPDATE portrait_builds SET status='OBSOLETE' WHERE build_id=? AND status IN ('QUEUED','RUNNING')",
                (current["build_id"],),
            )
        if source_version_id is None:
            self.conn.exec_driver_sql(
                "UPDATE current_portrait_state SET source_resume_version_id=NULL,status='NO_SOURCE',build_id=NULL,portrait_id=NULL,failure_code=NULL WHERE singleton_key=1"
            )
            return self.portrait_read()["state"]
        projection = self.ensure_evidence_projection(source_version_id)
        if not projection["entries"]:
            self.conn.exec_driver_sql(
                "UPDATE current_portrait_state SET source_resume_version_id=?,status='EMPTY_SOURCE',build_id=NULL,portrait_id=NULL,failure_code=NULL WHERE singleton_key=1",
                (source_version_id,),
            )
            return self.portrait_read()["state"]
        build_id = str(uuid4())
        self.insert(
            "portrait_builds",
            {
                "build_id": build_id,
                "source_resume_version_id": source_version_id,
                "selection_revision": selection["revision"],
                "extraction_key": EXTRACTION_KEY,
                "trigger_mode": trigger_mode,
                "status": "QUEUED",
                "failure_code": None,
                "created_at": now,
                "configuration_key": None,
                "baseline_portrait_id": None,
                "reattachment_portrait_id": None,
                "plan": None,
                "result_portrait_id": None,
                "disposition": None,
            },
        )
        self.conn.exec_driver_sql(
            "UPDATE current_portrait_state SET source_resume_version_id=?,status='QUEUED',build_id=?,portrait_id=NULL,failure_code=NULL WHERE singleton_key=1",
            (source_version_id, build_id),
        )
        return self.portrait_read()["state"]

    def portrait_value(self, portrait_id: str) -> Json:
        row = self.row(
            "SELECT portrait FROM portraits WHERE portrait_id=?", (portrait_id,), required=True
        )
        assert row is not None
        return checked(Portrait, decoded(row["portrait"]))

    def portrait_build(self, build_id: str) -> Json:
        row = self.row("SELECT * FROM portrait_builds WHERE build_id=?", (build_id,), required=True)
        assert row is not None
        if row.get("plan") is not None:
            row["plan"] = checked(DerivationPlan, decoded(row["plan"]))
        return row

    def build_plan(self, build_id: str, configuration_key: str) -> Json:
        build = self.row(
            "SELECT * FROM portrait_builds WHERE build_id=?", (build_id,), required=True
        )
        assert build is not None
        if build["plan"] is not None:
            if build["configuration_key"] != configuration_key:
                raise Failure("INVALID_STATE")
            return checked(DerivationPlan, decoded(build["plan"]))
        current = self.portrait_read()["state"]
        selection = self.selection()
        if (
            build["status"] != "QUEUED"
            or current["build_id"] != build_id
            or current["source_resume_version_id"] != build["source_resume_version_id"]
            or selection["revision"] != build["selection_revision"]
        ):
            raise Failure("INVALID_STATE")
        target = CandidateEvidenceProjection.model_validate(
            self.evidence_projection(build["source_resume_version_id"])
        )
        resume_id = self.conn.exec_driver_sql(
            "SELECT resume_id FROM resume_versions WHERE resume_version_id=?",
            (target.resume_version_id,),
        ).scalar_one()
        baseline: Portrait | None = None
        exact = False
        if build["trigger_mode"] == "AUTOMATIC":
            portrait_id = self.conn.exec_driver_sql(
                "SELECT portrait_id FROM portrait_derivations "
                "WHERE resume_id=? AND resume_version_id=? AND extraction_key=? "
                "AND configuration_key=? ORDER BY derivation_order DESC LIMIT 1",
                (resume_id, target.resume_version_id, target.extraction_key, configuration_key),
            ).scalar()
            if portrait_id is not None:
                baseline = Portrait.model_validate(self.portrait_value(portrait_id))
                exact = True
            else:
                portrait_id = self.conn.exec_driver_sql(
                    "SELECT portrait_id FROM portrait_derivations "
                    "WHERE resume_id=? AND extraction_key=? AND configuration_key=? "
                    "ORDER BY derivation_order DESC LIMIT 1",
                    (resume_id, target.extraction_key, configuration_key),
                ).scalar()
                if portrait_id is not None:
                    baseline = Portrait.model_validate(self.portrait_value(portrait_id))
        plan = make_plan(
            build_id=build_id,
            trigger_mode=build["trigger_mode"],
            configuration_key=configuration_key,
            target=target,
            baseline=baseline,
            exact_reattachment=exact,
        ).model_dump(mode="json")
        self.conn.exec_driver_sql(
            "UPDATE portrait_builds SET configuration_key=?,baseline_portrait_id=?,"
            "reattachment_portrait_id=?,plan=? WHERE build_id=? AND plan IS NULL",
            (
                configuration_key,
                plan["baseline_portrait_id"],
                plan["reattachment_portrait_id"],
                encoded(plan),
                build_id,
            ),
        )
        return plan

    def complete_zero_call(self, build_id: str, now: str) -> Json:
        build = self.row(
            "SELECT * FROM portrait_builds WHERE build_id=?", (build_id,), required=True
        )
        assert build is not None
        if build["plan"] is None:
            raise Failure("INVALID_STATE")
        plan = DerivationPlan.model_validate(decoded(build["plan"]))
        if plan.generated_entry_ids:
            raise Failure("INVALID_STATE")
        current = self.portrait_read()["state"]
        selection = self.selection()
        if (
            build["status"] != "QUEUED"
            or current["build_id"] != build_id
            or current["source_resume_version_id"] != plan.target_resume_version_id
            or selection["revision"] != build["selection_revision"]
        ):
            raise Failure("INVALID_STATE")
        if plan.reattachment_portrait_id is not None:
            portrait = self.portrait_value(plan.reattachment_portrait_id)
            result_id = plan.reattachment_portrait_id
            disposition = "REATTACHED"
        else:
            if plan.baseline_portrait_id is None:
                raise Failure("INVALID_STATE")
            evidence = CandidateEvidenceProjection.model_validate(
                self.evidence_projection(plan.target_resume_version_id)
            )
            profile = assemble_profile(plan, evidence, None)
            if not profile.entries:
                self.conn.exec_driver_sql(
                    "UPDATE portrait_builds SET status='FAILED',failure_code='OUTPUT_INVALID' "
                    "WHERE build_id=?",
                    (build_id,),
                )
                self.conn.exec_driver_sql(
                    "UPDATE current_portrait_state SET status='FAILED',portrait_id=NULL,"
                    "failure_code='OUTPUT_INVALID' WHERE singleton_key=1",
                )
                return self.portrait_read()["state"]
            result_id = str(uuid4())
            portrait = Portrait.model_validate(
                {
                    "portrait_id": result_id,
                    "schema_version": 1,
                    "resume_version_id": evidence.resume_version_id,
                    "extraction_key": evidence.extraction_key,
                    "profile": profile.model_dump(mode="json"),
                    "evidence": evidence.model_dump(mode="json"),
                    "generation": {
                        "kind": "REUSE",
                        "run_id": None,
                        "reused_from_portrait_id": plan.baseline_portrait_id,
                    },
                    "created_at": now,
                }
            ).model_dump(mode="json")
            self.insert(
                "portraits",
                {
                    "portrait_id": result_id,
                    "resume_version_id": evidence.resume_version_id,
                    "extraction_key": evidence.extraction_key,
                    "portrait": encoded(portrait),
                    "created_at": now,
                },
            )
            order = int(
                self.conn.exec_driver_sql(
                    "SELECT coalesce(max(derivation_order),0) FROM portrait_derivations"
                ).scalar_one()
            )
            if order == MAX_REVISION:
                raise Failure("REVISION_EXHAUSTED")
            resume_id = self.conn.exec_driver_sql(
                "SELECT resume_id FROM resume_versions WHERE resume_version_id=?",
                (evidence.resume_version_id,),
            ).scalar_one()
            self.insert(
                "portrait_derivations",
                {
                    "portrait_id": result_id,
                    "resume_id": resume_id,
                    "resume_version_id": evidence.resume_version_id,
                    "extraction_key": evidence.extraction_key,
                    "configuration_key": plan.configuration_key,
                    "derivation_order": order + 1,
                    "created_at": now,
                },
            )
            disposition = "NEW_PAIR"
        self.conn.exec_driver_sql(
            "UPDATE portrait_builds SET status='SUCCEEDED',result_portrait_id=?,disposition=? "
            "WHERE build_id=?",
            (result_id, disposition, build_id),
        )
        self.conn.exec_driver_sql(
            "UPDATE current_portrait_state SET status='READY',portrait_id=?,failure_code=NULL "
            "WHERE singleton_key=1",
            (result_id,),
        )
        return self.portrait_read()["state"]

    def portrait_read(self) -> Json:
        row = self.row("SELECT * FROM current_portrait_state WHERE singleton_key=1", required=True)
        assert row is not None
        row.pop("singleton_key")
        row["default_resume_selection"] = self.selection()
        state = checked(CurrentPortraitState, row)
        portrait = None
        if state["status"] == "READY":
            stored = self.row(
                "SELECT portrait FROM portraits WHERE portrait_id=?",
                (state["portrait_id"],),
                required=True,
            )
            assert stored is not None
            portrait = checked(Portrait, decoded(stored["portrait"]))
        return checked(PortraitRead, {"state": state, "portrait": portrait})

    def record(self, command: str, digest: str, result: Json) -> None:
        snapshot = {
            key: value for key, value in result.items() if key not in ("request_id", "outcome")
        }
        resume_id = resume_version_id = default_id = source_id = build_id = None
        if "resume" in snapshot:
            resume_id = snapshot["resume"]["resume_id"]
            resume_version_id = snapshot.pop("resume_version")["resume_version_id"]
        if "default_resume_selection" in snapshot:
            default_id = snapshot["default_resume_selection"]["default_resume_id"]
        if "state" in snapshot:
            source_id = snapshot["state"]["source_resume_version_id"]
            build_id = snapshot["state"]["build_id"]
        self.insert(
            "candidate_command_receipts",
            {
                "request_id": result["request_id"],
                "command_type": command,
                "request_fingerprint": digest,
                "schema_version": 2,
                "outcome": result["outcome"],
                "result_snapshot": encoded(snapshot),
                "resume_id": resume_id,
                "resume_version_id": resume_version_id,
                "default_resume_id": default_id,
                "source_resume_version_id": source_id,
                "build_id": build_id,
            },
        )

    def receipt(self, request_id: str, command: str, digest: str) -> Json | None:
        row = self.row("SELECT * FROM candidate_command_receipts WHERE request_id=?", (request_id,))
        if row is None:
            return None
        if row["command_type"] != command or row["request_fingerprint"] != digest:
            raise Failure("REQUEST_CONFLICT")
        snapshot = decoded(row["result_snapshot"])
        if not isinstance(snapshot, dict):
            raise Failure("INTERNAL_ERROR")
        result: Json = {"request_id": request_id, "outcome": row["outcome"], **snapshot}
        if result["outcome"] not in RESULT_OUTCOMES[command]:
            raise Failure("INTERNAL_ERROR")
        if "resume" in result:
            result["resume_version"] = self.version(row["resume_version_id"], required=True)
            if result["resume"]["resume_id"] != row["resume_id"]:
                raise Failure("INTERNAL_ERROR")
        if "default_resume_selection" in result:
            if result["default_resume_selection"]["default_resume_id"] != row["default_resume_id"]:
                raise Failure("INTERNAL_ERROR")
        if "state" in result:
            if (
                result["state"]["source_resume_version_id"] != row["source_resume_version_id"]
                or result["state"]["build_id"] != row["build_id"]
            ):
                raise Failure("INTERNAL_ERROR")
        model = RESULT_MODELS.get(command)
        return checked(model, result) if model is not None else result

    def recognize(self) -> None:
        schema_seven = any(
            row[1] == "trigger_mode"
            for row in self.conn.exec_driver_sql("PRAGMA table_info(portrait_builds)").all()
        )
        selection = self.selection()
        current = self.portrait_read()["state"]
        expected_source = None
        if selection["default_resume_id"] is not None:
            expected_source = self.root(selection["default_resume_id"], required=True)[
                "current_resume_version_id"
            ]
        if current["source_resume_version_id"] != expected_source:
            raise Failure("INTERNAL_ERROR")
        for identity in self.conn.exec_driver_sql("SELECT resume_id FROM resumes").scalars():
            self.pair(identity)
        for identity in self.conn.exec_driver_sql(
            "SELECT resume_version_id FROM candidate_evidence_projections"
        ).scalars():
            self.evidence_projection(identity)
        active_builds = (
            self.conn.exec_driver_sql(
                "SELECT build_id FROM portrait_builds WHERE status IN ('QUEUED','RUNNING')"
            )
            .scalars()
            .all()
        )
        expected_active = (
            [current["build_id"]] if current["status"] in ("QUEUED", "RUNNING") else []
        )
        if active_builds != expected_active:
            raise Failure("INTERNAL_ERROR")
        if current["build_id"] is not None:
            build = self.row(
                "SELECT * FROM portrait_builds WHERE build_id=?",
                (current["build_id"],),
                required=True,
            )
            assert build is not None
            expected_status = {
                "QUEUED": "QUEUED",
                "RUNNING": "RUNNING",
                "READY": "SUCCEEDED",
                "FAILED": "FAILED",
            }[current["status"]]
            if (
                build["source_resume_version_id"] != expected_source
                or build["selection_revision"] != selection["revision"]
                or build["status"] != expected_status
                or build["failure_code"] != current["failure_code"]
            ):
                raise Failure("INTERNAL_ERROR")
        for row in self.conn.exec_driver_sql("SELECT * FROM portrait_builds").mappings():
            if row["extraction_key"] != EXTRACTION_KEY:
                raise Failure("INTERNAL_ERROR")
            self.evidence_projection(row["source_resume_version_id"])
            if row["status"] == "FAILED" and not row["failure_code"]:
                raise Failure("INTERNAL_ERROR")
            if row["status"] != "FAILED" and row["failure_code"] is not None:
                raise Failure("INTERNAL_ERROR")
            if schema_seven:
                if row["trigger_mode"] not in ("AUTOMATIC", "FULL"):
                    raise Failure("INTERNAL_ERROR")
                if (row["configuration_key"] is None) != (row["plan"] is None):
                    raise Failure("INTERNAL_ERROR")
                if row["plan"] is not None:
                    plan = checked(DerivationPlan, decoded(row["plan"]))
                    if (
                        plan["build_id"] != row["build_id"]
                        or plan["trigger_mode"] != row["trigger_mode"]
                        or plan["target_resume_version_id"] != row["source_resume_version_id"]
                        or plan["configuration_key"] != row["configuration_key"]
                        or plan["baseline_portrait_id"] != row["baseline_portrait_id"]
                        or plan["reattachment_portrait_id"] != row["reattachment_portrait_id"]
                    ):
                        raise Failure("INTERNAL_ERROR")
        if schema_seven:
            orders: list[int] = []
            for row in self.conn.exec_driver_sql(
                "SELECT * FROM portrait_derivations ORDER BY derivation_order"
            ).mappings():
                portrait = self.portrait_value(row["portrait_id"])
                owner = self.conn.exec_driver_sql(
                    "SELECT resume_id FROM resume_versions WHERE resume_version_id=?",
                    (portrait["resume_version_id"],),
                ).scalar_one()
                if (
                    row["resume_id"] != owner
                    or row["resume_version_id"] != portrait["resume_version_id"]
                    or row["extraction_key"] != portrait["extraction_key"]
                ):
                    raise Failure("INTERNAL_ERROR")
                orders.append(row["derivation_order"])
            if orders != list(range(1, len(orders) + 1)):
                raise Failure("INTERNAL_ERROR")
