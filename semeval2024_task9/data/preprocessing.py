"""Preprocessing helpers for multiple-choice and binary-classification variants."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def build_multichoice_features(examples: Mapping[str, list[Any]], tokenizer):
    """Tokenize question/choice pairs in the notebook's multiple-choice layout."""

    first_sentences = [[question] * 4 for question in examples["question"]]
    first_sentences = sum(first_sentences, [])
    second_sentences = [choices for choices in examples["choice_list"]]
    second_sentences = sum(second_sentences, [])
    tokenized_examples = tokenizer(first_sentences, second_sentences, truncation=True)
    return {key: [value[i : i + 4] for i in range(0, len(value), 4)] for key, value in tokenized_examples.items()}


def create_binary_pairs(row: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Transform one multiple-choice row into binary question/answer pairs."""

    identifier = row["id"]
    question = str(row["question"]).strip()
    choices = list(row["choice_list"])
    correct_answer = choices[int(row["label"])]

    if not question.endswith("?"):
        question = f"{question}?"

    binary_pairs = []
    for index, choice in enumerate(choices):
        if "none of above" in str(choice).lower():
            continue
        formatted_choice = str(choice).strip()
        if not formatted_choice.endswith("."):
            formatted_choice = f"{formatted_choice}."
        label = 1 if choice == correct_answer else 0
        binary_pairs.append(
            {
                "id": f"{identifier}_{index}",
                "question": f"{question} {formatted_choice}",
                "label": label,
            }
        )
    return binary_pairs


def build_binary_features(dataset) -> list[dict[str, Any]]:
    """Build binary-classification rows for every example in a dataset."""

    rows = []
    for row in dataset:
        rows.extend(create_binary_pairs(row))
    return rows
