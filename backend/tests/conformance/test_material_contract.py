"""Independent Materials command codec and closed logical-role value checks."""

import hashlib
from decimal import Decimal
from uuid import uuid4

import pytest
from jobhunter.domain.derived_work.models import RenderRequest, fingerprint
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.infrastructure.rendering.catalog import catalog
from pydantic import ValidationError


def test_material_fingerprint_has_independent_namespace_and_excludes_request_id() -> None:
    command = RenderRequest(
        request_id="10000000-0000-4000-8000-000000000000",
        resume_version_id="20000000-0000-4000-8000-000000000000",
        render_configuration_id="30000000-0000-4000-8000-000000000000",
    )
    # Spelled codec bytes independently; no production encoder in the expected value.
    expected = (
        b"JobHunter:SL02:Materials:1\n" + b"a3:s14:RENDER_REQUESTno2:s23:render_configuration_id"
        b"s36:30000000-0000-4000-8000-000000000000s17:resume_version_id"
        b"s36:20000000-0000-4000-8000-000000000000"
    )
    assert fingerprint(command) == hashlib.sha256(expected).hexdigest()
    assert fingerprint(command.model_copy(update={"request_id": str(uuid4())})) == fingerprint(
        command
    )


@pytest.mark.parametrize("bad", [True, "1", Decimal("1.00000000000000000000001")])
def test_schema_version_is_exact_integral_number(bad: object) -> None:
    configuration = catalog()[0].model_dump(mode="json")
    configuration["schema_version"] = bad
    with pytest.raises(ValidationError):
        RenderConfiguration.model_validate(configuration)


def test_every_logical_font_has_four_final_hashes() -> None:
    for configuration in catalog():
        for roles in configuration.fonts.model_dump().values():
            assert set(roles) == {"regular", "bold", "italic", "bold_italic"}
            assert all(len(digest) == 64 for digest in roles.values())
