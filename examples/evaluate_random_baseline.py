"""Evaluate random predictions with the package metrics."""

from pathlib import Path
from random import Random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semeval2024_task9.data import load_npy_dataset
from semeval2024_task9.evaluation import group_accuracy, instance_accuracy


def main() -> None:
    dataset = load_npy_dataset("SP", "test_labeled")
    rng = Random(42)
    labels = {row["id"]: row["label"] for row in dataset}
    predictions = {row["id"]: rng.randrange(4) for row in dataset}
    instance = instance_accuracy(list(labels.values()), list(predictions.values()))
    grouped = group_accuracy(labels, predictions, num_groups=3)
    print(f"Random instance accuracy: {instance}")
    print(f"Random Ori+Sem+Con group accuracy: {grouped.accuracy}")


if __name__ == "__main__":
    main()
