from __future__ import annotations

import pytest


def test_instance_accuracy_rounds_like_notebooks():
    from semeval2024_task9.evaluation import instance_accuracy

    assert instance_accuracy([1, 0, 2], [1, 3, 2]) == 0.667


def test_group_accuracy_scores_only_complete_correct_groups():
    from semeval2024_task9.evaluation import group_accuracy

    labels = {
        "SP-0": 1,
        "SP-0_SR": 1,
        "SP-0_CR": 2,
        "SP-1": 0,
        "SP-1_SR": 0,
        "SP-1_CR": 0,
    }
    predictions = {
        "SP-0": 1,
        "SP-0_SR": 1,
        "SP-0_CR": 3,
        "SP-1": 0,
        "SP-1_SR": 0,
        "SP-1_CR": 0,
    }

    ori_sem = group_accuracy(labels, predictions, num_groups=2)
    ori_sem_con = group_accuracy(labels, predictions, num_groups=3)

    assert ori_sem.accuracy == 1.0
    assert ori_sem.correct == 2
    assert ori_sem.total == 2
    assert ori_sem_con.accuracy == 0.5
    assert ori_sem_con.correct == 1
    assert ori_sem_con.wrong_ids == ["SP-0"]


def test_group_accuracy_rejects_invalid_group_size():
    from semeval2024_task9.evaluation import group_accuracy

    with pytest.raises(ValueError, match="num_groups"):
        group_accuracy({"SP-0": 0}, {"SP-0": 0}, num_groups=4)
