"""Preferences SQL within the caller-owned transaction."""

from sqlalchemy.engine import Connection

from jobhunter.domain.preferences.models import PreferenceSet, PreferenceSetVersion, SaveResult
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.preference_values import (
    root_row,
    version_row,
)


class PreferenceRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def current(self) -> tuple[PreferenceSet, PreferenceSetVersion] | None:
        rows = self.conn.exec_driver_sql("SELECT * FROM preference_sets").mappings().all()
        if not rows:
            if self.conn.exec_driver_sql(
                "SELECT 1 FROM preference_set_versions UNION ALL "
                "SELECT 1 FROM preference_save_receipts LIMIT 1"
            ).first():
                raise Failure("STORAGE_CORRUPT")
            return None
        if len(rows) != 1:
            raise Failure("STORAGE_CORRUPT")
        root = root_row(dict(rows[0]))
        try:
            version = self.version(root.current_preference_set_version_id)
        except Failure:
            raise Failure("STORAGE_CORRUPT") from None
        if (
            version.preference_set_id != root.preference_set_id
            or version.created_at != root.updated_at
        ):
            raise Failure("STORAGE_CORRUPT")
        return root, version

    def version(self, identity: str) -> PreferenceSetVersion:
        row = (
            self.conn.exec_driver_sql(
                "SELECT * FROM preference_set_versions WHERE preference_set_version_id=?",
                (identity,),
            )
            .mappings()
            .first()
        )
        if row is None:
            raise Failure("NOT_FOUND")
        version = version_row(dict(row))
        root = self.conn.exec_driver_sql(
            "SELECT created_at, updated_at FROM preference_sets WHERE preference_set_id=?",
            (version.preference_set_id,),
        ).first()
        if root is None or not root[0] <= version.created_at <= root[1]:
            raise Failure("STORAGE_CORRUPT")
        return version

    def receipt(self, request_id: str, digest: str) -> SaveResult | None:
        row = (
            self.conn.exec_driver_sql(
                "SELECT * FROM preference_save_receipts WHERE request_id=?", (request_id,)
            )
            .mappings()
            .first()
        )
        if row is None:
            return None
        if row["request_fingerprint"] != digest:
            raise Failure("REQUEST_CONFLICT")
        result = SaveResult.model_validate(
            {
                "preference_set_id": row["preference_set_id"],
                "preference_set_version_id": row["preference_set_version_id"],
                "revision": row["result_revision"],
                "outcome": row["outcome"],
            }
        )
        version = self.version(result.preference_set_version_id)
        current = self.current()
        if (
            current is None
            or result.preference_set_id != version.preference_set_id
            or result.revision > current[0].revision
        ):
            raise Failure("STORAGE_CORRUPT")
        return result

    def publish(self, root: PreferenceSet, version: PreferenceSetVersion, *, first: bool) -> None:
        if first:
            self.conn.exec_driver_sql(
                "INSERT INTO preference_sets VALUES (?,1,?,?,?,?)",
                (
                    root.preference_set_id,
                    root.current_preference_set_version_id,
                    root.revision,
                    root.created_at,
                    root.updated_at,
                ),
            )
        else:
            self.conn.exec_driver_sql(
                "UPDATE preference_sets SET current_preference_set_version_id=?, revision=?, "
                "updated_at=? WHERE preference_set_id=?",
                (
                    root.current_preference_set_version_id,
                    root.revision,
                    root.updated_at,
                    root.preference_set_id,
                ),
            )
        self.conn.exec_driver_sql(
            "INSERT INTO preference_set_versions VALUES (?,?,?,?)",
            (
                version.preference_set_version_id,
                version.preference_set_id,
                version.created_at,
                version.configuration.model_dump_json(),
            ),
        )

    def record(self, request_id: str, digest: str, result: SaveResult) -> None:
        self.conn.exec_driver_sql(
            "INSERT INTO preference_save_receipts VALUES (?,?,?,?,?,?)",
            (
                request_id,
                digest,
                result.preference_set_id,
                result.preference_set_version_id,
                result.revision,
                result.outcome,
            ),
        )
