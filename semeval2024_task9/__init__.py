"""Utilities for the AILS-NTUA SemEval-2024 Task 9 BrainTeaser system."""

from .data import load_npy_dataset, match_triplets, split_ori_sem_con
from .evaluation import GroupAccuracyResult, group_accuracy, instance_accuracy, write_codalab_submission

__version__ = "0.1.0"

__all__ = [
    "GroupAccuracyResult",
    "__version__",
    "group_accuracy",
    "instance_accuracy",
    "load_npy_dataset",
    "match_triplets",
    "split_ori_sem_con",
    "write_codalab_submission",
]
