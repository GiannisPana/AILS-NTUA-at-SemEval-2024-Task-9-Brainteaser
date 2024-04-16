"""Utilities for original / semantic / context BrainTeaser triplets."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def _has_suffix(record: Mapping[str, Any], suffix: str) -> bool:
    return str(record["id"]).endswith(suffix)


def split_ori_sem_con(dataset):
    """Split a dataset into original, semantic reconstruction, and context reconstruction rows."""

    original = dataset.filter(lambda row: not _has_suffix(row, "_SR") and not _has_suffix(row, "_CR"))
    semantic = dataset.filter(lambda row: _has_suffix(row, "_SR"))
    context = dataset.filter(lambda row: _has_suffix(row, "_CR"))
    return original, semantic, context


def _base_id(identifier: str) -> str:
    if identifier.endswith("_SR") or identifier.endswith("_CR"):
        return identifier.rsplit("_", 1)[0]
    return identifier


def match_triplets(
    original_ids: Iterable[str],
    semantic_ids: Iterable[str],
    context_ids: Iterable[str],
) -> dict[str, tuple[str, str]]:
    """Match original ids to their semantic and context reconstruction ids."""

    semantic_by_base = {_base_id(str(identifier)): str(identifier) for identifier in semantic_ids}
    context_by_base = {_base_id(str(identifier)): str(identifier) for identifier in context_ids}

    triplets: dict[str, tuple[str, str]] = {}
    for identifier in original_ids:
        base = str(identifier)
        if base not in semantic_by_base or base not in context_by_base:
            raise ValueError(f"Missing reconstruction pair for '{base}'")
        triplets[base] = (semantic_by_base[base], context_by_base[base])
    return triplets
