"""Encoder multiple-choice training helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EncoderMultichoiceConfig:
    """Configuration for encoder multiple-choice fine-tuning."""

    model_name: str = "FacebookAI/roberta-large"
    task: str = "SP"
    learning_rate: float = 2e-5
    batch_size: int = 8
    num_epochs: int = 3
    seed: int = 42


def tiny_multiple_choice_smoke_step() -> float:
    """Run one no-network forward/backward step on a tiny local BERT model."""

    import torch
    from transformers import BertConfig, BertForMultipleChoice

    config = BertConfig(
        hidden_size=8,
        num_hidden_layers=1,
        num_attention_heads=2,
        intermediate_size=16,
        vocab_size=64,
    )
    model = BertForMultipleChoice(config)
    input_ids = torch.randint(0, config.vocab_size, (4, 4, 6))
    attention_mask = torch.ones_like(input_ids)
    labels = torch.tensor([0, 1, 2, 3], dtype=torch.long)
    output = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
    output.loss.backward()
    return float(output.loss.detach())
