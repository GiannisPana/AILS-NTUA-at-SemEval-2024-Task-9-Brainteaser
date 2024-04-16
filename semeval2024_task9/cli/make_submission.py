"""Create a CodaLab-format answer file from integer predictions."""

from __future__ import annotations

import argparse
from pathlib import Path

from semeval2024_task9.evaluation import write_codalab_submission


def _read_predictions(path: Path) -> list[int]:
    return [int(line.strip()) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Write SemEval-2024 Task 9 CodaLab submission file.")
    parser.add_argument("--predictions", type=Path, required=True, help="Text file with one integer prediction per line.")
    parser.add_argument("--output", type=Path, required=True, help="Output answer file path.")
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    output = write_codalab_submission(_read_predictions(args.predictions), args.output)
    print(output)


if __name__ == "__main__":
    main()
