"""Accuracy metrics for BrainTeaser predictions."""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping, Sequence


@dataclass(frozen=True)
class GroupAccuracyResult:
    """Group-accuracy result."""

    accuracy: float
    correct: int
    total: int
    wrong_ids: list[str]


def instance_accuracy(labels: Sequence[int], predictions: Sequence[int]) -> float:
    """Return instance accuracy rounded to three decimals, matching the notebooks."""

    if len(labels) != len(predictions):
        raise ValueError("labels and predictions must have the same length")
    if not labels:
        return 0.0
    correct = sum(int(label) == int(prediction) for label, prediction in zip(labels, predictions))
    return round(correct / len(labels), 3)


def _base_ids(labels: Mapping[str, int]) -> list[str]:
    return sorted(identifier for identifier in labels if not identifier.endswith("_SR") and not identifier.endswith("_CR"))


def group_accuracy(
    labels: Mapping[str, int],
    predictions: Mapping[str, int],
    num_groups: int = 2,
) -> GroupAccuracyResult:
    """Compute original+semantic or original+semantic+context group accuracy."""

    if num_groups not in {2, 3}:
        raise ValueError("num_groups must be 2 or 3")

    correct = 0
    wrong_ids: list[str] = []
    bases = _base_ids(labels)

    for base in bases:
        required = [base, f"{base}_SR"]
        if num_groups == 3:
            required.append(f"{base}_CR")
        missing = [identifier for identifier in required if identifier not in labels or identifier not in predictions]
        if missing:
            raise ValueError(f"Missing labels or predictions for: {', '.join(missing)}")
        group_correct = all(int(labels[identifier]) == int(predictions[identifier]) for identifier in required)
        if group_correct:
            correct += 1
        else:
            wrong_ids.append(base)

    total = len(bases)
    accuracy = round(correct / total, 3) if total else 0.0
    return GroupAccuracyResult(accuracy=accuracy, correct=correct, total=total, wrong_ids=wrong_ids)
