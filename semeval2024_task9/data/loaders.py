"""Load SemEval-2024 Task 9 BrainTeaser NumPy files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable, Mapping
import warnings

import numpy as np

try:  # pragma: no cover - exercised when optional dependency is installed.
    from datasets import Dataset
except ImportError:  # pragma: no cover - covered through behavior tests.
    from .simple_dataset import SimpleDataset as Dataset
    _USING_SIMPLE_DATASET = True
else:
    _USING_SIMPLE_DATASET = False


_SPLIT_FILES = {
    "train": "{task}-train.npy",
    "test_labeled": "{task}_test_labeled.npy",
    "labeled_test": "{task}_test_labeled.npy",
    "test": "{task}_test.npy",
    "dev": "{task}_eval_data_for_practice.npy",
    "practice": "{task}_eval_data_for_practice.npy",
    "eval": "{task}_eval_data_for_practice.npy",
}


def _normalize_task(task: str) -> str:
    normalized = task.upper()
    if normalized not in {"SP", "WP"}:
        raise ValueError("task must be 'SP' or 'WP'")
    return normalized


def _path_for_split(task: str, split: str, data_dir: Path) -> Path:
    try:
        template = _SPLIT_FILES[split.lower()]
    except KeyError as exc:
        valid = ", ".join(sorted(_SPLIT_FILES))
        raise ValueError(f"Unsupported split '{split}'. Expected one of: {valid}") from exc
    return data_dir / template.format(task=task)


def _to_record(item: Any) -> dict[str, Any]:
    if hasattr(item, "item"):
        try:
            item = item.item()
        except ValueError:
            pass
    if isinstance(item, Mapping):
        return dict(item)
    raise ValueError(f"Expected dict-like dataset row, got {type(item).__name__}")


def _coerce_records(records: Iterable[dict[str, Any]], split: str) -> list[dict[str, Any]]:
    coerced = []
    for record in records:
        row = dict(record)
        if split == "train":
            for key in ["id", "distractor1", "distractor2", "distractor(unsure)"]:
                if key in row and row[key] is not None:
                    row[key] = str(row[key])
            if "label" in row:
                row["label"] = int(row["label"])
        elif split in {"test_labeled", "labeled_test"}:
            if "id" in row and row["id"] is not None:
                row["id"] = str(row["id"])
            if "label" in row:
                row["label"] = int(row["label"])
        coerced.append(row)
    return coerced


def load_npy_records(
    task: str,
    split: str = "train",
    data_dir: str | Path = "data",
) -> list[dict[str, Any]]:
    """Load a BrainTeaser split as a list of dictionaries."""

    normalized_task = _normalize_task(task)
    normalized_split = split.lower()
    path = _path_for_split(normalized_task, normalized_split, Path(data_dir))
    if not path.exists():
        raise FileNotFoundError(path)

    data = np.load(path, allow_pickle=True)
    records = [_to_record(item) for item in data]
    return _coerce_records(records, normalized_split)


def load_npy_dataset(
    task: str,
    split: str = "train",
    data_dir: str | Path = "data",
) -> Dataset:
    """Load a BrainTeaser split.

    Returns a Hugging Face ``Dataset`` after a normal package install. If the
    package was installed without dependencies, a small local fallback is used
    and a warning is emitted.
    """

    if _USING_SIMPLE_DATASET:
        warnings.warn(
            "Hugging Face 'datasets' is not installed; returning "
            "semeval2024_task9.data.SimpleDataset instead of datasets.Dataset.",
            RuntimeWarning,
            stacklevel=2,
        )
    return Dataset.from_list(load_npy_records(task=task, split=split, data_dir=data_dir))
