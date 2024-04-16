"""Prediction helpers for encoder multiple-choice models."""

from __future__ import annotations


def predict_multiple_choice_logits(logits):
    """Return the argmax class for a multiple-choice logits tensor."""

    return logits.argmax(dim=-1)
