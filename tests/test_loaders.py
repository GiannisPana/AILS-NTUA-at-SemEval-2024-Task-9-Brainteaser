from __future__ import annotations

import pytest

from tests.conftest import DATA_DIR


def test_load_npy_dataset_maps_train_split_and_preserves_fields():
    from semeval2024_task9.data import load_npy_dataset
    from datasets import Dataset

    dataset = load_npy_dataset("SP", "train", data_dir=DATA_DIR)

    assert isinstance(dataset, Dataset)
    assert len(dataset) == 507
    assert set(["id", "question", "choice_list", "label"]).issubset(dataset.column_names)
    assert dataset[0]["id"] == "SP-0"
    assert isinstance(dataset[0]["label"], int)
    assert len(dataset[0]["choice_list"]) == 4


def test_load_npy_dataset_maps_labeled_test_split():
    from semeval2024_task9.data import load_npy_dataset

    dataset = load_npy_dataset("WP", "test_labeled", data_dir=DATA_DIR)

    assert len(dataset) == 96
    assert set(["id", "question", "choice_list", "label", "answer"]).issubset(dataset.column_names)
    assert dataset[0]["id"] == "WP-140"


def test_load_npy_dataset_rejects_unknown_split():
    from semeval2024_task9.data import load_npy_dataset

    with pytest.raises(ValueError, match="Unsupported split"):
        load_npy_dataset("SP", "unknown", data_dir=DATA_DIR)
