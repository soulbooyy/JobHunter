"""Immutable configuration, contained provenance and published byte identity."""

from decimal import Decimal
from typing import Annotated, Literal, cast

from pydantic import BeforeValidator, Field

from jobhunter.domain.shared.values import DTO, UtcTimestamp, UuidV4, invalid, scalar


def integer(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, Decimal)):
        invalid("INVALID_TYPE")
    if isinstance(value, Decimal) and (not value.is_finite() or value != value.to_integral_value()):
        invalid("OUT_OF_RANGE")
    value = cast(int | Decimal, value)
    if value < 0:
        invalid("OUT_OF_RANGE")
    return int(value)


Positive = Annotated[int, Field(ge=1), BeforeValidator(integer)]
Nonnegative = Annotated[int, Field(ge=0), BeforeValidator(integer)]
Digest = Annotated[str, Field(pattern="^[0-9a-f]{64}$"), BeforeValidator(scalar)]
Key = Annotated[str, Field(pattern="^[a-z][a-z0-9_]{0,63}$"), BeforeValidator(scalar)]
Version = Annotated[
    str, Field(pattern="^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$"), BeforeValidator(scalar)
]


class Template(DTO):
    template_key: Key
    template_version: Version


class Renderer(DTO):
    pipeline_key: Key
    pipeline_version: Version


class FontRoles(DTO):
    regular: Digest
    bold: Digest
    italic: Digest
    bold_italic: Digest


class Fonts(DTO):
    SOURCE_HAN_SANS: FontRoles
    HEITI: FontRoles
    SONGTI: FontRoles
    KAITI: FontRoles


class PdfOutput(DTO):
    media_type: Literal["application/pdf"]


class PngOutput(DTO):
    media_type: Literal["image/png"]
    page_width_px: Positive


class RenderConfiguration(DTO):
    render_configuration_id: UuidV4
    schema_version: Annotated[Literal[1], BeforeValidator(integer)]
    template: Template
    renderer: Renderer
    fonts: Fonts
    output: Annotated[PdfOutput | PngOutput, Field(discriminator="media_type")]


class ConfigurationAvailability(DTO):
    configuration: RenderConfiguration
    can_generate: bool


class ConfigurationList(DTO):
    items: list[ConfigurationAvailability]


class RenderManifest(DTO):
    schema_version: Annotated[Literal[2], BeforeValidator(integer)]
    resume_id: UuidV4
    resume_version_id: UuidV4
    render_configuration_id: UuidV4
    artifact_id: UuidV4


class Artifact(DTO):
    artifact_id: UuidV4
    schema_version: Annotated[Literal[2], BeforeValidator(integer)]
    manifest: RenderManifest
    media_type: Literal["application/pdf", "image/png"]
    byte_length: Annotated[int, Field(ge=1, le=9007199254740991), BeforeValidator(integer)]
    sha256: Digest
    created_at: UtcTimestamp
