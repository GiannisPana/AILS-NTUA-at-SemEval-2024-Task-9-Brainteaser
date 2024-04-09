# Model Training
The notebooks corresponding to the fine-tuning of encoder models and LLMs for model evaluation are organized as follows:

| Notebook                                                               | Description                                                     |
|------------------------------------------------------------------------|-----------------------------------------------------------------|
| [small_models_hyperparameter_search](./small_models_hyperparameter_search.ipynb) | Hyperparameter search for small encoder models.                 |
| [small_models_training_multiple_choice](./small_models_training_multiple_choice.ipynb) | Training small encoder models for multi-class classification.   |
| [small_models_training_text_classification](./small_models_training_text_classification.ipynb) | Training small encoder models for binary text classification.   |
| [QLoRA_LLMs_finetuning_multiple_choice](./QLoRA_LLMs_finetuning_multiple_choice.ipynb) | Fine-tuning LLMs for multi-class classification tasks.          |
| [QLoRA_LLMs_finetuning_text_classification](./QLoRA_LLMs_finetuning_text_classification.ipynb) | Fine-tuning LLMs for binary text classification tasks.          |

**Important Notes:**

1. Each notebook specifies the model used for fine-tuning within its contents.

2. Binary classification results for LLMs are excluded from our submission due to suboptimal performance compared to multi-class classification. However, we've included this setup for completeness and reproducibility purposes.

3. Metrics calculation for instance-based and group-based evaluation are implemented within each model's notebook. Additionally, we've included logic for exporting test set results in the format required by the CodaLab competition.