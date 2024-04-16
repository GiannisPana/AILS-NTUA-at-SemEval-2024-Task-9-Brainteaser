"""Small local dataset fallback used when Hugging Face datasets is unavailable."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any


class SimpleDataset:
    """A tiny subset of the Hugging Face Dataset API used by this repository."""

    def __init__(self, rows: list[dict[str, Any]]):
        self._rows = rows
        keys: list[str] = []
        for row in rows:
            for key in row:
                if key not in keys:
                    keys.append(key)
        self.column_names = keys

    @classmethod
    def from_list(cls, rows: list[dict[str, Any]]) -> "SimpleDataset":
        return cls(rows)

    def __len__(self) -> int:
        return len(self._rows)

    def __iter__(self) -> Iterator[dict[str, Any]]:
        return iter(self._rows)

    def __getitem__(self, key):
        if isinstance(key, str):
            return [row[key] for row in self._rows]
        return self._rows[key]

    def filter(self, predicate: Callable[[dict[str, Any]], bool]) -> "SimpleDataset":
        return SimpleDataset([row for row in self._rows if predicate(row)])

    def to_list(self) -> list[dict[str, Any]]:
        return list(self._rows)
