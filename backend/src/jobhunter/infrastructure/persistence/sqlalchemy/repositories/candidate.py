"""Relational saved-authority persistence; validate stored bodies at the read boundary."""

import json
from decimal import Decimal, DecimalException
from typing import Any, cast

from pydantic import BaseModel, ValidationError
from sqlalchemy.engine import Connection

from jobhunter.domain.evidence import models as ev
from jobhunter.domain.profile import models as pr
from jobhunter.domain.resume import models as rs
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.workspace.selection import DefaultSelection

Json = dict[str, Any]
ROOT_MODELS: dict[str, type[BaseModel]] = {
    "profile": pr.Profile,
    "evidence_item": ev.EvidenceItem,
    "resume": rs.Resume,
}
VERSION_MODELS: dict[str, type[BaseModel]] = {
    "profile": pr.ProfileVersion,
    "evidence_item": ev.EvidenceVersion,
    "resume": rs.ResumeVersion,
}
RESULT_MODELS: dict[str, type[BaseModel]] = {
    "PROFILE_SAVE": pr.ProfileResult,
    "EVIDENCE_CREATE": ev.EvidenceResult,
    "EVIDENCE_UPDATE": ev.EvidenceResult,
    "EVIDENCE_RETIRE": ev.EvidenceResult,
    "RESUME_CREATE": rs.ResumeSelectionResult,
    "RESUME_REMOVE": rs.ResumeSelectionResult,
    "RESUME_SAVE": rs.ResumeResult,
    "RESUME_RENAME": rs.ResumeResult,
    "DEFAULT_RESUME_SET": rs.SelectionResult,
}
REFERENCE_COLUMNS = (
    "profile_id",
    "profile_version_id",
    "evidence_item_id",
    "evidence_item_version_id",
    "evidence_baseline_snapshot_id",
    "resume_id",
    "resume_version_id",
    "default_resume_id",
)


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
        # Identifiers originate exclusively from this repository/application, never HTTP input.
        self.conn.exec_driver_sql(
            f"INSERT INTO {table} ({','.join(data)}) VALUES ({','.join('?' for _ in data)})",
            tuple(data.values()),
        )

    def root(self, name: str, identity: str | None = None, *, required: bool = False) -> Json:
        row = self.row(
            f"SELECT * FROM {name}s WHERE "
            + ("singleton_key=1" if identity is None else f"{name}_id=?"),
            () if identity is None else (identity,),
            required=required or name == "profile",
        )
        if row is None:
            raise Failure("NOT_FOUND")
        row.pop("singleton_key", None)
        return checked(ROOT_MODELS[name], row)

    def version(self, name: str, identity: str, *, required: bool = False) -> Json:
        row = self.row(
            f"SELECT * FROM {name}_versions WHERE {name}_version_id=?",
            (identity,),
            required=required,
        )
        if row is None:
            raise Failure("NOT_FOUND")
        root = self.root(name, row[name + "_id"], required=True)
        if name == "evidence_item":
            row["fields"] = checked(ev.FIELD_MODELS[root["kind"]], decoded(row["fields"]))
            row["content"] = decoded(row["content"])
        elif name == "resume":
            row["header_presentation"] = decoded(row["header_presentation"])
            row["document_presentation"] = decoded(row["document_presentation"])
            self.version("profile", row["profile_version_id"], required=True)
            sections: list[Json] = []
            for section in self.conn.exec_driver_sql(
                (
                    "SELECT position,kind FROM resume_sections WHERE resume_version_id=? ORDER "
                    "BY position"
                ),
                (identity,),
            ).mappings():
                if section["position"] != len(sections):
                    raise Failure("INTERNAL_ERROR")
                members: list[Json] = []
                for member in self.conn.exec_driver_sql(
                    (
                        "SELECT * FROM resume_members WHERE resume_version_id=? AND "
                        "section_position=? ORDER BY position"
                    ),
                    (identity, section["position"]),
                ).mappings():
                    if member["position"] != len(members) or member["kind"] != section["kind"]:
                        raise Failure("INTERNAL_ERROR")
                    source = self.version(
                        "evidence_item", member["evidence_item_version_id"], required=True
                    )
                    source_root = self.root(
                        "evidence_item", member["evidence_item_id"], required=True
                    )
                    if (
                        source["evidence_item_id"] != member["evidence_item_id"]
                        or source_root["kind"] != section["kind"]
                    ):
                        raise Failure("INTERNAL_ERROR")
                    members.append(
                        {
                            "evidence_item_id": member["evidence_item_id"],
                            "evidence_item_version_id": member["evidence_item_version_id"],
                            "content": decoded(member["content"]),
                        }
                    )
                sections.append({"kind": section["kind"], "members": members})
            row["sections"] = sections
        row = checked(VERSION_MODELS[name], row)
        if row["created_at"] < root["created_at"] or row["created_at"] > root["updated_at"]:
            raise Failure("INTERNAL_ERROR")
        return row

    def pair(self, name: str, identity: str | None = None) -> Json:
        root = self.root(name, identity)
        version = self.version(name, root["current_" + name + "_version_id"], required=True)
        if version[name + "_id"] != root[name + "_id"]:
            raise Failure("INTERNAL_ERROR")
        return {name: root, name + "_version": version}

    def selection(self) -> Json:
        row = self.row(
            "SELECT default_resume_id,revision FROM default_resume_selection WHERE singleton_key=1",
            required=True,
        )
        assert row is not None
        row = checked(DefaultSelection, row)
        count = self.count("resume")
        if row["default_resume_id"] is None:
            if count != 0:
                raise Failure("INTERNAL_ERROR")
        elif self.root("resume", row["default_resume_id"], required=True)["status"] != "ACTIVE":
            raise Failure("INTERNAL_ERROR")
        return row

    def set_selection(self, selection: Json) -> None:
        self.conn.exec_driver_sql(
            (
                "UPDATE default_resume_selection SET default_resume_id=?,revision=? WHERE "
                "singleton_key=1"
            ),
            (selection["default_resume_id"], selection["revision"]),
        )

    def count(self, name: str) -> int:
        return int(
            self.conn.exec_driver_sql(
                f"SELECT count(*) FROM {name}s WHERE status='ACTIVE'"
            ).scalar_one()
        )

    def baseline(self, identity: str | None = None) -> Json:
        current = identity is None
        if identity is None:
            pointer = self.row(
                (
                    "SELECT evidence_baseline_snapshot_id FROM current_evidence_baseline WHERE "
                    "singleton_key=1"
                ),
                required=True,
            )
            assert pointer is not None
            identity = pointer["evidence_baseline_snapshot_id"]
        row = self.row(
            "SELECT * FROM evidence_baselines WHERE evidence_baseline_snapshot_id=?",
            (identity,),
            required=current,
        )
        if row is None:
            raise Failure("NOT_FOUND")
        row["members"] = [
            dict(m)
            for m in self.conn.exec_driver_sql(
                (
                    "SELECT evidence_item_id,evidence_item_version_id FROM "
                    "evidence_baseline_members WHERE evidence_baseline_snapshot_id=? ORDER BY "
                    "evidence_item_id"
                ),
                (identity,),
            ).mappings()
        ]
        for member in row["members"]:
            version = self.version(
                "evidence_item", member["evidence_item_version_id"], required=True
            )
            if (
                version["evidence_item_id"] != member["evidence_item_id"]
                or version["created_at"] > row["created_at"]
            ):
                raise Failure("INTERNAL_ERROR")
        if current and row["members"] != self.active_members():
            raise Failure("INTERNAL_ERROR")
        return checked(ev.Baseline, row)

    def active_members(self) -> list[Json]:
        return [
            dict(m)
            for m in self.conn.exec_driver_sql(
                "SELECT evidence_item_id,current_evidence_item_version_id AS "
                "evidence_item_version_id FROM evidence_items WHERE status='ACTIVE' ORDER "
                "BY evidence_item_id"
            ).mappings()
        ]

    def publish_baseline(self, identity: str, now: str) -> None:
        self.insert(
            "evidence_baselines",
            {"evidence_baseline_snapshot_id": identity, "schema_version": 1, "created_at": now},
        )
        for member in self.active_members():
            self.insert(
                "evidence_baseline_members", {"evidence_baseline_snapshot_id": identity, **member}
            )
        self.conn.exec_driver_sql(
            (
                "UPDATE current_evidence_baseline SET evidence_baseline_snapshot_id=? WHERE "
                "singleton_key=1"
            ),
            (identity,),
        )

    def publish(self, name: str, root: Json, version: Json | None, *, first: bool = False) -> None:
        if first:
            self.insert(name + "s", root)
        else:
            values = {k: v for k, v in root.items() if k != name + "_id"}
            self.conn.exec_driver_sql(
                f"UPDATE {name}s SET {','.join(k + '=?' for k in values)} WHERE {name}_id=?",
                (*values.values(), root[name + "_id"]),
            )
        if version is None:
            return
        data = dict(version)
        sections: list[Json] = []
        if name == "evidence_item":
            data["fields"], data["content"] = encoded(data["fields"]), encoded(data["content"])
        elif name == "resume":
            sections = data.pop("sections")
            data["header_presentation"] = encoded(data["header_presentation"])
            data["document_presentation"] = encoded(data["document_presentation"])
        self.insert(name + "_versions", data)
        for position, section in enumerate(sections):
            self.insert(
                "resume_sections",
                {
                    "resume_version_id": data["resume_version_id"],
                    "position": position,
                    "kind": section["kind"],
                },
            )
            for index, member in enumerate(section["members"]):
                self.insert(
                    "resume_members",
                    {
                        "resume_version_id": data["resume_version_id"],
                        "section_position": position,
                        "position": index,
                        "kind": section["kind"],
                        **member,
                        "content": encoded(member["content"]),
                    },
                )

    def references(self, snapshot: Json) -> Json:
        refs: Json = dict.fromkeys(REFERENCE_COLUMNS)
        for name in ("profile", "evidence_item", "resume"):
            if name in snapshot:
                refs[name + "_id"] = snapshot[name][name + "_id"]
                refs[name + "_version_id"] = snapshot[name + "_version_id"]
        if "evidence_baseline_snapshot_id" in snapshot:
            refs["evidence_baseline_snapshot_id"] = snapshot["evidence_baseline_snapshot_id"]
        if "default_resume_selection" in snapshot:
            refs["default_resume_id"] = snapshot["default_resume_selection"]["default_resume_id"]
        return refs

    def record(self, command: str, digest: str, result: Json) -> None:
        checked(RESULT_MODELS[command], result)
        snapshot = {k: v for k, v in result.items() if k not in ("request_id", "outcome")}
        for name in ("profile", "evidence_item", "resume"):
            if name + "_version" in snapshot:
                snapshot[name + "_version_id"] = snapshot.pop(name + "_version")[
                    name + "_version_id"
                ]
        self.insert(
            "candidate_command_receipts",
            {
                "request_id": result["request_id"],
                "command_type": command,
                "request_fingerprint": digest,
                "schema_version": 1,
                "outcome": result["outcome"],
                "result_snapshot": encoded(snapshot),
                **self.references(snapshot),
            },
        )

    def receipt(self, request_id: str, command: str, digest: str) -> Json | None:
        row = self.row("SELECT * FROM candidate_command_receipts WHERE request_id=?", (request_id,))
        if row is None:
            return None
        if row["command_type"] != command or row["request_fingerprint"] != digest:
            raise Failure("REQUEST_CONFLICT")
        snapshot = decoded(row["result_snapshot"])
        if not isinstance(snapshot, dict) or self.references(cast(Json, snapshot)) != {
            k: row[k] for k in REFERENCE_COLUMNS
        }:
            raise Failure("INTERNAL_ERROR")
        snapshot = cast(Json, snapshot)
        result: Json = {"request_id": request_id, "outcome": row["outcome"], **snapshot}
        for name in ("profile", "evidence_item", "resume"):
            if name in snapshot:
                root = checked(ROOT_MODELS[name], snapshot[name])
                version_id = result.pop(name + "_version_id", None)
                version = self.version(name, version_id, required=True)
                if (
                    root["current_" + name + "_version_id"] != version_id
                    or version[name + "_id"] != root[name + "_id"]
                    or version["created_at"] > root["updated_at"]
                ):
                    raise Failure("INTERNAL_ERROR")
                result[name + "_version"] = version
        if "evidence_baseline_snapshot_id" in snapshot:
            try:
                self.baseline(snapshot["evidence_baseline_snapshot_id"])
            except Failure:
                raise Failure("INTERNAL_ERROR") from None
        if "default_resume_selection" in snapshot:
            selection = checked(DefaultSelection, snapshot["default_resume_selection"])
            if selection["default_resume_id"] is not None:
                self.root("resume", selection["default_resume_id"], required=True)
        return checked(RESULT_MODELS[command], result)

    def recognize(self) -> None:
        self.pair("profile")
        self.baseline()
        self.selection()
