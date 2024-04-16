"""Print one original / semantic / context triplet."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from semeval2024_task9.data import load_npy_dataset, match_triplets, split_ori_sem_con


def main() -> None:
    dataset = load_npy_dataset("SP", "train")
    original, semantic, context = split_ori_sem_con(dataset)
    triplets = match_triplets(original["id"], semantic["id"], context["id"])
    base, (semantic_id, context_id) = next(iter(triplets.items()))
    rows = {row["id"]: row for row in dataset}
    for identifier in [base, semantic_id, context_id]:
        print(f"{identifier}: {rows[identifier]['question']}")


if __name__ == "__main__":
    main()
