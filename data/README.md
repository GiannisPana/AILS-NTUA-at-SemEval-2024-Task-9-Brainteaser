# Data Overview
The data contained in this directory are as follows:

- Semeval Competition
  - Training Data
    - `SP_train.npy` (Semeval training data)
    - `WP_train.npy` (Semeval training data)
  - Development Data
    - `SP_eval_data_for_practice.npy` (Semeval development data)
    - `WP_eval_data_for_practice.npy` (Semeval development data)
  - Test Data
    - `SP_test.npy` (Semeval test data)
    - `WP_test.npy` (Semeval test data)
    - `SP_test_answer.npy` (Semeval test data answer)
    - `WP_test_answer.npy` (Semeval test data answer)
    - `SP_test_labeled.npy` (Semeval test data with labels)
    - `WP_test_labeled.npy` (Semeval test data with labels)

Each question in the dataset provides four options, one of which is the correct answer, and the rest serve as **distractors**. Additionally, there is always a fourth option, "None of above".

In addition to the original puzzles, the dataset includes adversarial subsets created by modifying the brain teasers while preserving their reasoning paths. This includes:

- **Semantic Reconstruction**: Original questions are rephrased semantically without changing answers or distractors.
  
- **Context Reconstruction**: Original reasoning paths are retained but the brain teaser describes a new situational context.

The dataset used for training, evaluation and testing consists of triplets of data (original, semantic reconstruction, context reconstruction)

The dataset splits and details for each subtask are summarized in the following table:

| **Sub-task**         | **Train**          | **Dev**         | **Test**         |
|----------------------|--------------------|-----------------|------------------|
| A - Sentence Puzzle  | 507 (3 x 169)      | 120 (3 x 40)    | 120 (3 x 40)     |
| B - Word Puzzle      | 396 (3 x 132)      | 96  (3 x 32)    | 96  (3 x 32)     |


### Train Dataset Format (with an example)

```json
{
  "id": "WP-0",
  "question": "How do you spell COW in thirteen letters?",
  "answer": "SEE O DOUBLE YOU.",
  "distractor1": "COWCOWCOWCOWW",
  "distractor2": "SEE OH DEREFORD",
  "distractor(unsure)": "None of above.",
  "label": 1,
  "choice_list": [
    "SEE OH DEREFORD",
    "SEE O DOUBLE YOU.",
    "COWCOWCOWCOWW",
    "None of above."
  ],
  "choice_order": [2, 0, 1, 3]
}
```

### Test Dataset Format (with an example)
The presented dataset format represent the result of preprocessing both the test data and their corresponding answers separately. Subsequently, these processed datasets were merged to form the structured format outlined.

```json
{
  "id": "WP-87_SR",
  "question": "What do you call a toothless bear?",
  "choice_list": [
    "A brown bear.",
    "A polar bear.",
    "A gummy bear.",
    "None of above."
  ],
  "label": 2,
  "answer": "A gummy bear."
}
```

### Explanation

1. **Train Dataset**:
   - Each entry (`id`) represents a question-answer pair with additional information.
   - The `question` field contains the question prompt.
   - `answer` is the correct answer to the question.
   - `distractor1`, `distractor2`, and `distractor(unsure)` are incorrect options.
   - `label` indicates the index (0-based) of the correct answer within `choice_list`.
   - `choice_list` provides all answer options in a fixed order.
   - `choice_order` specifies the correct answer's position within `choice_list`.

2. **Test Dataset**:
   - Similar to the train dataset but lacks the `answer` and `label` fields.
   - `label` is replaced by the `answer` field, which holds the correct answer for each question.
   - The `choice_list` includes multiple answer options without specific order indication.

**Transformation to Binary Classification**:
- For each unique `id` in the training dataset, we transform the multi-class problem into multiple binary classification tasks.
- This involves creating binary labels (`label`) where:
  - `label` is `1` if the model's prediction matches the correct answer.
  - `label` is `0` otherwise (for each option other than the correct answer).
- This approach allows the model to learn and predict correctness based on the available answer choices, effectively converting the multi-class problem into a set of binary classification tasks per question.