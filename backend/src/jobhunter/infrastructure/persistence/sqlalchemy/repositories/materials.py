"""Retained configuration, demand and artifact metadata; payloads have a separate owner."""

from typing import cast

from sqlalchemy.engine import Connection

from jobhunter.domain.derived_work.models import (
    Accepted,
    RenderIntent,
    RenderRequest,
    Work,
    fingerprint,
)
from jobhunter.domain.materials.models import Artifact, RenderConfiguration
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import (
    CandidateRepository,
    Json,
    checked,
    decoded,
    encoded,
)


class MaterialsRepository(CandidateRepository):
    def __init__(self, conn: Connection) -> None:
        super().__init__(conn)

    def configuration(self, identity: str) -> Json:
        row = self.row(
            "SELECT * FROM render_configurations WHERE render_configuration_id=?", (identity,)
        )
        if row is None:
            raise Failure("NOT_FOUND")
        value = checked(RenderConfiguration, decoded(row["configuration"]))
        if value["render_configuration_id"] != identity:
            raise Failure("INTERNAL_ERROR")
        return value

    def register(self, configuration: RenderConfiguration) -> None:
        identity = configuration.render_configuration_id
        if (
            self.row(
                "SELECT 1 FROM render_configurations WHERE render_configuration_id=?", (identity,)
            )
            is not None
        ):
            if self.configuration(identity) != configuration.model_dump(mode="json"):
                raise Failure("INTERNAL_ERROR")
            return
        self.insert(
            "render_configurations",
            {
                "render_configuration_id": identity,
                "configuration": encoded(configuration.model_dump(mode="json")),
            },
        )

    def work(self, identity: str) -> Json:
        row = self.row("SELECT * FROM render_work WHERE work_id=?", (identity,), required=True)
        assert row is not None
        return checked(Work, row)

    def intent(self, identity: str) -> Json:
        row = self.row("SELECT * FROM render_intents WHERE render_intent_id=?", (identity,))
        if row is None:
            raise Failure("NOT_FOUND")
        row.pop("work_id")
        return checked(RenderIntent, row)

    def artifact(self, identity: str) -> Json:
        row = self.row("SELECT * FROM artifacts WHERE artifact_id=?", (identity,))
        if row is None:
            raise Failure("NOT_FOUND")
        sections: list[Json] = []
        for source in self.conn.exec_driver_sql(
            "SELECT * FROM artifact_sources WHERE artifact_id=? ORDER BY "
            "section_position,member_position",
            (identity,),
        ).mappings():
            position = source["section_position"]
            if position == len(sections):
                sections.append({"kind": source["kind"], "evidence_refs": []})
            if (
                position >= len(sections)
                or source["member_position"]
                != len(cast(list[Json], sections[position]["evidence_refs"]))
                or source["kind"] != sections[position]["kind"]
            ):
                raise Failure("INTERNAL_ERROR")
            cast(list[Json], sections[position]["evidence_refs"]).append(
                {
                    "evidence_item_id": source["evidence_item_id"],
                    "evidence_item_version_id": source["evidence_item_version_id"],
                }
            )
        manifest = {
            key: row[key]
            for key in (
                "schema_version",
                "resume_id",
                "resume_version_id",
                "profile_version_id",
                "render_configuration_id",
                "artifact_id",
            )
        }
        manifest["source_sections"] = sections
        result = {
            key: row[key]
            for key in (
                "artifact_id",
                "schema_version",
                "media_type",
                "byte_length",
                "sha256",
                "created_at",
            )
        }
        result["manifest"] = manifest
        result = checked(Artifact, result)
        try:
            configuration = self.configuration(row["render_configuration_id"])
        except Failure:
            raise Failure("INTERNAL_ERROR") from None
        if configuration["output"]["media_type"] != row["media_type"]:
            raise Failure("INTERNAL_ERROR")
        # Provenance must cover all saved membership; no rendering/body dependency here.
        expected = self.conn.exec_driver_sql(
            "SELECT section_position,position,evidence_item_id,evidence_item_version_id FROM "
            "resume_members WHERE resume_version_id=? ORDER BY section_position,position",
            (row["resume_version_id"],),
        ).all()
        actual = self.conn.exec_driver_sql(
            "SELECT section_position,member_position,evidence_item_id,evidence_item_version_id "
            "FROM artifact_sources WHERE artifact_id=? ORDER BY section_position,member_position",
            (identity,),
        ).all()
        if expected != actual:
            raise Failure("INTERNAL_ERROR")
        return result

    def replay(self, command: RenderRequest) -> Json | None:
        row = self.row(
            "SELECT * FROM material_command_receipts WHERE operation='RENDER_REQUEST' AND "
            "request_id=?",
            (command.request_id,),
        )
        if row is None:
            return None
        result = checked(Accepted, decoded(row["result_snapshot"]))
        try:
            intent = self.intent(row["render_intent_id"])
        except Failure:
            raise Failure("INTERNAL_ERROR") from None
        original = RenderRequest(
            request_id=row["request_id"],
            resume_version_id=intent["resume_version_id"],
            render_configuration_id=intent["render_configuration_id"],
        )
        if (
            result["request_id"] != row["request_id"]
            or result["render_intent_id"] != row["render_intent_id"]
            or row["schema_version"] != 1
            or fingerprint(original) != row["request_fingerprint"]
        ):
            raise Failure("INTERNAL_ERROR")
        if row["request_fingerprint"] != fingerprint(command):
            raise Failure("REQUEST_CONFLICT")
        return result

    def recognize_materials(self) -> None:
        if (
            self.conn.exec_driver_sql(
                "SELECT 1 FROM render_intents i LEFT JOIN material_command_receipts r "
                "ON r.render_intent_id=i.render_intent_id WHERE r.request_id IS NULL LIMIT 1"
            ).first()
            or self.conn.exec_driver_sql(
                "SELECT 1 FROM render_work w LEFT JOIN render_intents i ON i.work_id=w.work_id "
                "WHERE i.render_intent_id IS NULL LIMIT 1"
            ).first()
        ):
            raise Failure("INTERNAL_ERROR")
        for identity in self.conn.exec_driver_sql(
            "SELECT render_configuration_id FROM render_configurations"
        ).scalars():
            self.configuration(identity)
        for identity in self.conn.exec_driver_sql("SELECT work_id FROM render_work").scalars():
            self.work(identity)
        for identity in self.conn.exec_driver_sql(
            "SELECT render_intent_id FROM render_intents"
        ).scalars():
            self.intent(identity)
        for identity in self.conn.exec_driver_sql("SELECT artifact_id FROM artifacts").scalars():
            self.artifact(identity)
        for row in self.conn.exec_driver_sql(
            "SELECT request_id,render_intent_id FROM material_command_receipts"
        ).mappings():
            intent = self.intent(row["render_intent_id"])
            self.replay(
                RenderRequest(
                    request_id=row["request_id"],
                    resume_version_id=intent["resume_version_id"],
                    render_configuration_id=intent["render_configuration_id"],
                )
            )
        if self.conn.exec_driver_sql(
            "SELECT 1 FROM render_intents i JOIN render_work w ON i.work_id=w.work_id WHERE "
            "(i.status='PENDING' AND w.status NOT IN ('QUEUED','RUNNING')) OR "
            "(i.status='FULFILLED' AND w.status!='SUCCEEDED') OR (i.status='FAILED' AND "
            "w.status!='FAILED') LIMIT 1"
        ).first():
            raise Failure("INTERNAL_ERROR")
