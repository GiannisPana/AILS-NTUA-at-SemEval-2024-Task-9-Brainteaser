# AILS-NTUA at SemEval-2024 Task 9: BrainTeaser

*A fine-tuned Mistral-7B QLoRA system beat the paper's ChatGPT baseline by nearly 20 points on Sentence Puzzle and over 30 on Word Puzzle.*

[![Paper](https://img.shields.io/badge/Paper-ACL%20Anthology-blue)](https://aclanthology.org/2024.semeval-1.248/)
[![PDF](https://img.shields.io/badge/PDF-ACL%20Anthology-red)](https://aclanthology.org/2024.semeval-1.248.pdf)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](pyproject.toml)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

[Paper](https://aclanthology.org/2024.semeval-1.248/) | [PDF](https://aclanthology.org/2024.semeval-1.248.pdf) | [arXiv](https://arxiv.org/abs/2404.01084) | [Usage](docs/USAGE.md) | [Data](data/README.md) | [Reproducing](docs/REPRODUCING.md) | [Citation](#citation)

---

<p align="center">
  <img src="assets/our-best-vs-baselines.svg" alt="AILS-NTUA best systems compared with human, ChatGPT, and RoBERTa-large baselines">
</p>

---

## The Task

BrainTeaser evaluates lateral thinking through original riddles and two adversarial variants that preserve the reasoning path. In the paper's example, the original asks *"What kind of nut has no shell?"* with **A doughnut** as the answer; the semantic reconstruction asks *"Which nut doesn't have a shell?"* with the same answer; the context reconstruction asks *"Which type of bell doesn't make a sound?"* with **A bluebell** as the answer. A system must solve the surface form and keep the reasoning pattern stable across the original, semantic, and context variants.

## Results

On the SemEval-2024 Task 9 evaluation split, the best submitted AILS-NTUA systems reported in the paper were:

| Sub-task | Our best | ChatGPT | Human | Gap vs ChatGPT |
|---|---:|---:|---:|---:|
| Sentence Puzzle | **81.7%** (Mistral-7B QLoRA, r=128, alpha=128) | 62.7% | 92.0% | +19.0 pts |
| Word Puzzle | **85.4%** (Mistral-7B QLoRA, r=16, alpha=64) | 53.5% | 91.7% | +31.9 pts |

- The Sentence Puzzle score is one of three Mistral-7B QLoRA configurations tied at 81.7% in Table 4.
- At the matched r=128, alpha=128 LoRA configuration, Mistral-7B beats the paper's 8x larger Mixtral-8x7B comparison by +1.7 points on Sentence Puzzle and +17.7 on Word Puzzle.
- Fine-tuned encoders also beat ChatGPT in the reported overall metric: RoBERTa-WNGRD reaches 78.4% on Sentence Puzzle and DeBERTaV3-base reaches 68.7% on Word Puzzle.

Full model tables and the LoRA-configuration plots are in [docs/PAPER_RESULTS.md](docs/PAPER_RESULTS.md).

## Quickstart

```bash
git clone https://github.com/GiannisPana/AILS-NTUA-at-SemEval-2024-Task-9-Brainteaser.git
cd AILS-NTUA-at-SemEval-2024-Task-9-Brainteaser
```

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

```python
from semeval2024_task9.data import load_npy_dataset

sp_train = load_npy_dataset("SP", "train")
print(len(sp_train), sp_train[0])
```

For full training reproduction, use the notebooks in [model_training](model_training/README.md). The extracted Python package currently covers data loading, triplet handling, metrics, submission formatting, and CPU-importable encoder scaffolding. QLoRA training extraction is deferred until GPU verification is available.

## How It Works

The system explores two paths: encoder fine-tuning for multiple-choice and binary classification variants, and QLoRA fine-tuning of LLMs for the original multiple-choice formulation. Evaluation uses both instance accuracy and group accuracy over original plus semantic, or original plus semantic plus context reconstructions.

## Docs

- [Installation and usage](docs/USAGE.md)
- [Dataset structure](data/README.md)
- [Paper results and plots](docs/PAPER_RESULTS.md)
- [Reproducing experiments](docs/REPRODUCING.md)
- [Runnable examples](examples/README.md)

<details>
<summary>Repository map</summary>

```text
semeval2024_task9/
  data/          loaders, triplet splitting, preprocessing helpers
  evaluation/    instance/group metrics and CodaLab submission output
  models/        multiple-choice data collator
  training/      CPU-importable encoder scaffolding
  inference/     encoder prediction helpers
  cli/           command-line wrappers
model_training/  original Colab/Kaggle notebooks
data/            BrainTeaser train/dev/test NumPy files
docs/            usage, reproduction, and result notes
assets/          README and documentation figures
examples/        small runnable examples
tests/           focused package tests
```

[Package overview](semeval2024_task9/README.md) | [data](semeval2024_task9/data/README.md) | [evaluation](semeval2024_task9/evaluation/README.md) | [models](semeval2024_task9/models/README.md) | [training](semeval2024_task9/training/README.md) | [inference](semeval2024_task9/inference/README.md)

</details>

## Citation

*Ioannis Panagiotopoulos, Giorgos Filandrianos, Maria Lymperaiou, Giorgos Stamou - AILS Lab, National Technical University of Athens. SemEval 2024.*

```bibtex
@inproceedings{panagiotopoulos-etal-2024-ails,
  title = "{AILS}-{NTUA} at {S}em{E}val-2024 Task 9: Cracking Brain Teasers: Transformer Models for Lateral Thinking Puzzles",
  author = "Panagiotopoulos, Ioannis and Filandrianos, George and Lymperaiou, Maria and Stamou, Giorgos",
  booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
  month = jun,
  year = "2024",
  address = "Mexico City, Mexico",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2024.semeval-1.248/",
  doi = "10.18653/v1/2024.semeval-1.248",
  pages = "1733--1746"
}
```

## License

Code and documentation authored in this repository are released under the MIT License. The BrainTeaser/SemEval data files under `data/` remain governed by upstream terms; see [NOTICE](NOTICE), the [BrainTeaser organizer repository](https://github.com/1171-jpg/BrainTeaser), and the [SemEval-2024 Task 9 paper](https://aclanthology.org/2024.semeval-1.274/).
