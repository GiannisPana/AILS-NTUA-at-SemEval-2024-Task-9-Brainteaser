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


