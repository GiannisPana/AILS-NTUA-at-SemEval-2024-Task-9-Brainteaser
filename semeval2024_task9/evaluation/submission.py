"""CodaLab submission formatting."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


def write_codalab_submission(predictions: Iterable[int], output_file: str | Path) -> Path:
    """Write one integer prediction per line, matching the original notebooks."""

    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for predicted_class in predictions:
            file.write(f"{int(predicted_class)}\n")
    return path
