from __future__ import annotations

import pytest


def test_tiny_multiple_choice_smoke_step_runs_without_network():
    pytest.importorskip("torch")
    pytest.importorskip("transformers")

    from semeval2024_task9.training import tiny_multiple_choice_smoke_step

    loss = tiny_multiple_choice_smoke_step()

    assert loss > 0
