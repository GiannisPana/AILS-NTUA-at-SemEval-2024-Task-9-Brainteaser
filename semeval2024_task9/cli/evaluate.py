"""Small metric CLI for saved labels and predictions."""

from __future__ import annotations

import argparse
from pathlib import Path

from semeval2024_task9.evaluation import instance_accuracy


def _read_ints(path: Path) -> list[int]:
    return [int(line.strip()) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compute instance accuracy from label and prediction files.")
    parser.add_argument("--labels", type=Path, required=True, help="Text file with one gold integer label per line.")
    parser.add_argument("--predictions", type=Path, required=True, help="Text file with one predicted integer label per line.")
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    print(instance_accuracy(_read_ints(args.labels), _read_ints(args.predictions)))


if __name__ == "__main__":
    main()
