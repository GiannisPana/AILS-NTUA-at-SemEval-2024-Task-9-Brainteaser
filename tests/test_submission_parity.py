from __future__ import annotations

import numpy as np

from tests.conftest import DATA_DIR


def test_write_codalab_submission_matches_notebook_one_label_per_line(tmp_path):
    from semeval2024_task9.evaluation import write_codalab_submission

    output = tmp_path / "answer_sen.txt"
    write_codalab_submission([2, 0, 3], output)

    assert output.read_text(encoding="utf-8") == "2\n0\n3\n"


def test_write_codalab_submission_preserves_answer_file_order(tmp_path):
    from semeval2024_task9.evaluation import write_codalab_submission

    answer_rows = np.load(DATA_DIR / "SP_test_answer.npy", allow_pickle=True)
    labels_in_source_order = [int(row[1]) for row in answer_rows]
    output = tmp_path / "answer_sen.txt"

    write_codalab_submission(labels_in_source_order, output)

    assert output.read_text(encoding="utf-8").splitlines() == [
        str(row[1]) for row in answer_rows
    ]
