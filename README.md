# AILS-NTUA at SemEval-2024: Task 9-Brainteaser
<!-- Our SemEval-2024 Task 9 competition code repository. -->

### This repository houses the data and code related to our submission for the SemEval-2024 Task 9 competition titled "BRAINTEASER: A Novel Task Defying Common Sense". 
### For a comprehensive overview of our system, refer to our ***[system description paper](https://arxiv.org/abs/2404.01084)***.

Feel free to explore our implementation, data resources, and findings documented in this repository. If you have any questions or feedback, please reach out. We hope our contribution advances the understanding and exploration of this intriguing task.


- **Task Description Paper**: Explore the task description in detail by referring to [this paper](https://aclanthology.org/2024.semeval2024-1.271).
- **Dataset Construction Details**: For insights into how the dataset was constructed, refer to the EMNLP 2023 paper available [here](https://arxiv.org/abs/2310.05057).
- **Official Task Organizer Repository**: Visit the [organizer's repository](https://github.com/1171-jpg/BrainTeaser) for the official source of the task materials and updates.



### 1. **Data**
The data for the BrainTeaser dataset is organized into two subtasks: 
1. Sentence Puzzle (Sub-task A)
2. Word Puzzle (Sub-task B). 

You can access the dataset in the ***[data directory](./data/)***, where detailed information about the dataset files is available.


### 2. Techniques Overview

1. **Encoder Model Fine-Tuning**:
   - We fine-tuned BERT, RoBERTa-large, and DeBERTaV3-base encoder models to assess transfer learning effects across datasets with similar reasoning requirements to BrainTeaser. For each encoder, we explored two approaches:
     - **Vanilla Model**: Fine-tuned solely on BrainTeaser data using default pre-trained weights.
     - **Extended Pre-training Model**: Pre-trained on additional commonsense reasoning datasets before fine-tuning on BrainTeaser data.
   
   We investigated both the original multi-choice setup and a transformed binary classification task to analyze various reasoning strategies effectively.

2. **Language Model (LLM) Fine-Tuning**:
   - We fine-tuned LLMs (Llama 2, Phi-2, Mistral-7b) on the BrainTeaser dataset, leveraging their demonstrated enhanced reasoning capabilities, and evaluated their performance on the test set.

These techniques enabled us to explore different training approaches and evaluate model performance within the context of the BrainTeaser task. Explore our notebooks for detailed implementations and results. 


### The implementation code related to the mentioned techniques is located in the ***[model_training directory](./model_training/)***. 
#### Detailed information about each notebook's functionality and methodology can be explored within the aforementioned directory.

### 3. **Evaluation Metrics:**

Both sub-tasks are assessed using accuracy metrics in two ways. 

- **Instance-based accuracy** evaluates individual questions and their adversarials, providing insights into a model's reasoning proficiency across scenarios.

- **Group-based accuracy** assesses questions in cohesive groups of three, evaluating a model's ability to solve all questions within a group, reflecting holistic performance in lateral thinking challenges.

These combined metrics offer comprehensive insights into the capabilities of participating systems across both sub-tasks.

The calculation of these metrics is implemented within the model training notebooks, providing a detailed evaluation of model performance.

### 4. **Important Notes:**

1. The notebooks were developed using the Hugging Face Transformers library and PyTorch, ensuring compatibility with cutting-edge NLP research.

2. Our experiments were conducted on Google Colab and Kaggle, utilizing their GPU resources for efficient model training and evaluation. You can easily replicate our experiments by importing the notebooks into these platforms.

3. Detailed hyperparameters and model configurations are specified in our system description paper. For a comprehensive overview of our setup, refer to the paper alongside the notebooks.


### Cite
```
@misc{panagiotopoulos2024ailsntua,
      title={AILS-NTUA at SemEval-2024 Task 9: Cracking Brain Teasers: Transformer Models for Lateral Thinking Puzzles}, 
      author={Ioannis Panagiotopoulos and Giorgos Filandrianos and Maria Lymperaiou and Giorgos Stamou},
      year={2024},
      eprint={2404.01084},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

