"""Load a BrainTeaser split and print a few rows."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semeval2024_task9.data import load_npy_dataset


def main() -> None:
    dataset = load_npy_dataset("SP", "train")
    print(f"SP train rows: {len(dataset)}")
    for row in list(dataset)[:3]:
        print(row["id"], row["question"])


if __name__ == "__main__":
    main()
