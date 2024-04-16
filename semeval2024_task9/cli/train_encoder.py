"""Encoder training CLI placeholder."""

from __future__ import annotations

import argparse

from semeval2024_task9.training import EncoderMultichoiceConfig


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Configure encoder fine-tuning for SemEval-2024 Task 9.")
    parser.add_argument("--model", default=EncoderMultichoiceConfig.model_name)
    parser.add_argument("--task", choices=["SP", "WP"], default=EncoderMultichoiceConfig.task)
    parser.add_argument("--learning-rate", type=float, default=EncoderMultichoiceConfig.learning_rate)
    parser.add_argument("--batch-size", type=int, default=EncoderMultichoiceConfig.batch_size)
    parser.add_argument("--num-epochs", type=int, default=EncoderMultichoiceConfig.num_epochs)
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    config = EncoderMultichoiceConfig(
        model_name=args.model,
        task=args.task,
        learning_rate=args.learning_rate,
        batch_size=args.batch_size,
        num_epochs=args.num_epochs,
    )
    print(config)


if __name__ == "__main__":
    main()
