# Data

The data package loads the local BrainTeaser `.npy` files and exposes helpers
for the original, semantic reconstruction, and context reconstruction triplets.

```python
from semeval2024_task9.data import load_npy_dataset, split_ori_sem_con

train = load_npy_dataset("SP", "train")
original, semantic, context = split_ori_sem_con(train)
```

Supported split names are `train`, `test_labeled`, `test`, and `dev`.
