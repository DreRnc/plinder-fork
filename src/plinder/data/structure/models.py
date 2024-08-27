# Copyright (c) 2024, Plinder Development Team
# Distributed under the terms of the Apache License 2.0
from __future__ import annotations

from enum import Enum
from functools import cached_property
from typing import List

from pydantic import BaseModel, ConfigDict

DOCKQ_BACKBONE_ATOMS = ["C", "CA", "N", "O"]


class Base(BaseModel):
    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, use_enum_values=True
    )


class ChainConfig(Base):
    """Preparation configuration settings.

    Default configuration for preparation of normalized monomers,
    ready for use in PPI generation tasks.
    """

    decoy_receptor: List[str] = ["R"]
    decoy_ligand: List[str] = ["L"]
    native_receptor: List[str] = ["R"]
    native_ligand: List[str] = ["L"]


class BackboneDefinition(str, Enum):
    # Biotite (standard) C, CA, N
    biotite = "biotite"
    # DockQ definition: C, CA, N, O
    dockq = "dockq"


class DatasetName(str, Enum):
    plinder_s = "plinder_s"
    plinder_xl = "plinder_xl"
    plinder_af2 = "plinder_af2"


class MonomerName(str, Enum):
    holo = "holo"
    apo = "apo"
    predicted = "predicted"


class DocBaseModel(BaseModel):
    @classmethod
    def get_docstrings(cls) -> list[tuple[str, str | None]]:
        """
        Returns a list of all properties in the class.

        Returns:
        --------
        list
            A list of tuples containing the name and docstring of each property.
        """
        attributes = [
            (name, value.description) for name, value in cls.model_fields.items()
        ]
        others = [
            (name, prop.__doc__)
            for name, prop in cls.__dict__.items()
            if isinstance(prop, cached_property) or isinstance(prop, property)
        ]
        return attributes + others
