"""Admit persisted Preferences without treating JSON spelling as authority."""

import json
from datetime import datetime
from decimal import Decimal

from sqlalchemy.engine import Connection

from jobhunter.domain.preferences.models import (
    Configuration,
    PreferenceSet,
    PreferenceSetVersion,
    SaveResult,
)
from jobhunter.domain.shared.errors import Failure


def timestamp(value: str) -> None:
    datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")


def version_row(row: dict[str, object]) -> PreferenceSetVersion:
    try:
        raw = row["configuration"]
        if not isinstance(raw, str):
            raise ValueError()
        configuration: object = json.loads(raw, parse_float=Decimal, parse_int=Decimal)
        admitted = Configuration.model_validate(configuration)
        if admitted.model_dump() != configuration:
            raise ValueError()
        result = PreferenceSetVersion.model_validate({**row, "configuration": admitted})
        timestamp(result.created_at)
        return result
    except Exception:
        raise Failure("STORAGE_CORRUPT") from None


def root_row(row: dict[str, object]) -> PreferenceSet:
    try:
        result = PreferenceSet.model_validate(
            {k: v for k, v in row.items() if k != "singleton_key"}
        )
        timestamp(result.created_at)
        timestamp(result.updated_at)
        if result.updated_at < result.created_at:
            raise ValueError()
        return result
    except Exception:
        raise Failure("STORAGE_CORRUPT") from None


def recognize_values(conn: Connection) -> None:
    roots = [
        root_row(dict(r)) for r in conn.exec_driver_sql("SELECT * FROM preference_sets").mappings()
    ]
    versions = {
        v.preference_set_version_id: v
        for v in (
            version_row(dict(r))
            for r in conn.exec_driver_sql("SELECT * FROM preference_set_versions").mappings()
        )
    }
    if len(roots) > 1 or (not roots and versions):
        raise Failure("STORAGE_CORRUPT")
    for root in roots:
        current = versions.get(root.current_preference_set_version_id)
        if (
            current is None
            or current.preference_set_id != root.preference_set_id
            or current.created_at != root.updated_at
        ):
            raise Failure("STORAGE_CORRUPT")
        if any(
            v.preference_set_id != root.preference_set_id
            or not root.created_at <= v.created_at <= root.updated_at
            for v in versions.values()
        ):
            raise Failure("STORAGE_CORRUPT")
    try:
        for row in conn.exec_driver_sql("SELECT * FROM preference_save_receipts").mappings():
            result = SaveResult.model_validate(
                {
                    "preference_set_id": row["preference_set_id"],
                    "preference_set_version_id": row["preference_set_version_id"],
                    "revision": row["result_revision"],
                    "outcome": row["outcome"],
                }
            )
            version = versions.get(result.preference_set_version_id)
            if (
                version is None
                or version.preference_set_id != result.preference_set_id
                or not roots
                or result.revision > roots[0].revision
            ):
                raise ValueError()
    except Exception:
        raise Failure("STORAGE_CORRUPT") from None
