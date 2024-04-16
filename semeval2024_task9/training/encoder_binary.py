"""Encoder binary-classification training helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EncoderBinaryConfig:
    """Configuration for encoder binary-classification fine-tuning."""

    model_name: str = "FacebookAI/roberta-large"
    task: str = "SP"
    learning_rate: float = 2e-5
    batch_size: int = 8
    num_epochs: int = 3
    seed: int = 42
