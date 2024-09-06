# Copyright (c) 2024, Plinder Development Team
# Distributed under the terms of the Apache License 2.0
from __future__ import annotations

from functools import cached_property
from pathlib import Path

from pydantic import BaseModel


class DocBaseModel(BaseModel):
    @classmethod
    def get_descriptions_and_types(cls) -> dict[str, tuple[str | None, str | None]]:
        """
        Returns a dictionary mapping attribute and property names to their descriptions and types.

        Returns:
        --------
        dict[str, str | None]
            A dictionary mapping attribute and property names to their descriptions and types.
        """
        descriptions = {}
        annotations = cls.__annotations__
        for name, value in cls.model_fields.items():
            descriptions[name] = (value.description, annotations[name])

        for name, prop in cls.__dict__.items():
            if isinstance(prop, cached_property) or isinstance(prop, property):
                descriptions[name] = (
                    prop.__doc__,
                    prop.func.__annotations__.get("return", None)
                    if hasattr(prop, "func")
                    else None,
                )
        return descriptions

    @classmethod
    def document_properties_to_tsv(cls, prefix: str, filename: Path) -> None:
        with open(filename, "w") as tsv:
            # write header
            tsv.write("\t".join(["Name", "Type", "Description"]) + "\n")
            # write fields info
            for field, field_info in cls.get_descriptions_and_types().items():
                description, dtype = field_info
                if field.startswith(prefix):
                    name = field
                else:
                    name = f"{prefix}_{field}"
                if description:
                    descr = description.lstrip().replace("\n", " ")
                    if descr.startswith("__"):
                        continue
                else:
                    descr = "[DESCRIPTION MISSING]"
                if "pass_criteria" in name and "validation" not in name:
                    name = name.replace("pass_criteria", "pass_validation_criteria")
                tsv.write("\t".join([name, str(dtype), descr]) + "\n")