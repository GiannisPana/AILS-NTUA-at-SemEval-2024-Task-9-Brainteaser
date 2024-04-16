# Usage

This guide keeps installation and runnable commands separate from the root README.

## Installation

Create a local environment and install the package. The base install includes
`datasets`, so `load_npy_dataset()` returns a Hugging Face `Dataset`.

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\python -m pip install -e .
```

macOS/Linux:

```bash
python3 -m venv venv
./venv/bin/python -m pip install -e .
```

For encoder experiments, use the 2024-compatible encoder environment:

```bash
pip install -r requirements-encoders.txt
```

For QLoRA notebooks, use a separate environment:

```bash
pip install -r requirements-qlora.txt
```

The two requirement files intentionally use different `datasets` versions because
the original notebooks were developed with different stacks.

## Python API

```python
from semeval2024_task9.data import load_npy_dataset, split_ori_sem_con
from semeval2024_task9.evaluation import instance_accuracy, group_accuracy

train = load_npy_dataset("SP", "train")
original, semantic, context = split_ori_sem_con(train)

labels = {"SP-0": 1, "SP-0_SR": 1}
predictions = {"SP-0": 1, "SP-0_SR": 1}
print(group_accuracy(labels, predictions, num_groups=2))
```

## CLI

```bash
semeval2024-evaluate --labels labels.txt --predictions predictions.txt
semeval2024-make-submission --predictions predictions.txt --output submission/answer_sen.txt
semeval2024-train-encoder --help
```

## Notebook Path

The original training notebooks remain under `model_training/` and are the
faithful Colab/Kaggle reproduction path. The package provides reusable data,
metric, and submission utilities around that notebook logic.

## Troubleshooting

- If `pip install -e .` fails due to missing build tools, install `wheel` in the
  environment and retry.
- QLoRA training requires GPU/CUDA support and the pinned `requirements-qlora.txt`
  environment.
- The package can load local `.npy` data without downloading anything from the
  Hugging Face Hub.
