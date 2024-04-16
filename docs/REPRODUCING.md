# Reproducing Paper Runs

The original experiments were run in Google Colab and Kaggle. This repository
keeps the notebooks untouched and adds reusable package helpers for loading data,
metrics, and submission formatting.

## Recommended Order

1. Install the package with `pip install -e .`.
2. Inspect the local data with `python examples/load_and_inspect_data.py`.
3. Open the relevant notebook in `model_training/`.
4. Use `requirements-encoders.txt` for encoder notebooks and
   `requirements-qlora.txt` for QLoRA notebooks.
5. Record model names, LoRA rank/alpha, task, and run date in any new result
   files.

## Encoder Settings

The paper appendix reports AdamW with a linear scheduler. BERT and BERT-SE use a
learning rate of `3e-5`, batch size `16`, and `3` epochs. RoBERTa-large and
RoBERTa-WNGRD use the same setting. DeBERTaV3 variants use the same setup except
for batch size `4`.

## QLoRA Settings

The notebooks explore Llama 2, Phi-2, Mistral-7B, and Mixtral-8x7B with LoRA
rank and alpha combinations. Mixtral-8x7B is reported at `r=128`, `alpha=128`,
dropout `0.1`, learning rate `2e-5`, batch size `2`, and `250` training steps.

## Outputs

The submission writer preserves the notebook format: one integer prediction per
line, in test-set order. Use:

```bash
semeval2024-make-submission --predictions predictions.txt --output submission/answer_sen.txt
```

## Limits

QLoRA extraction is intentionally marked as deferred until GPU verification is
available. The notebooks remain the source of truth for full QLoRA reproduction.
