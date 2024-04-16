# semeval2024_task9 Package

This package contains reusable utilities extracted from the AILS-NTUA
SemEval-2024 Task 9 BrainTeaser notebooks.

## Public API

```python
from semeval2024_task9.data import load_npy_dataset, split_ori_sem_con
from semeval2024_task9.evaluation import instance_accuracy, group_accuracy
```

The current package focuses on data loading, triplet handling, metrics, and
submission formatting. Encoder training helpers are provided separately from the
original notebooks; QLoRA extraction is intentionally deferred until GPU
verification is available.
