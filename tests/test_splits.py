from __future__ import annotations

from tests.conftest import DATA_DIR


def test_split_ori_sem_con_separates_train_triplet_variants():
    from semeval2024_task9.data import load_npy_dataset, split_ori_sem_con

    dataset = load_npy_dataset("SP", "train", data_dir=DATA_DIR)
    original, semantic, context = split_ori_sem_con(dataset)

    assert len(original) == 169
    assert len(semantic) == 169
    assert len(context) == 169
    assert all("_SR" not in row["id"] and "_CR" not in row["id"] for row in original)
    assert all(row["id"].endswith("_SR") for row in semantic)
    assert all(row["id"].endswith("_CR") for row in context)


def test_match_triplets_returns_semantic_and_context_ids_for_each_original():
    from semeval2024_task9.data import load_npy_dataset, match_triplets, split_ori_sem_con

    dataset = load_npy_dataset("SP", "train", data_dir=DATA_DIR)
    original, semantic, context = split_ori_sem_con(dataset)
    triplets = match_triplets(original["id"], semantic["id"], context["id"])

    assert len(triplets) == 169
    assert triplets["SP-0"] == ("SP-0_SR", "SP-0_CR")
    assert all(len(pair) == 2 for pair in triplets.values())
