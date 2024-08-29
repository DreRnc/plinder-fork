# Copyright (c) 2024, Plinder Development Team
# Distributed under the terms of the Apache License 2.0
from textwrap import dedent

try:
    import ost  # noqa
except (ImportError, ModuleNotFoundError):
    raise ImportError(
        dedent(
            """\
            plinder.eval requires the OpenStructureToolkit >= 2.8.0 (ost) to be installed.
            Please refer to the documentation for installation instructions and current limitations.
            See the note here: https://github.com/plinder-org/plinder?tab=readme-ov-file#-getting-started
            """
        )
    )
