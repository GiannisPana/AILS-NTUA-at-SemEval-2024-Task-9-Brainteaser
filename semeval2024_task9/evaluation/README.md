# Evaluation

The evaluation helpers expose the two BrainTeaser metrics used in the notebooks
and paper:

- `instance_accuracy`: accuracy over individual multiple-choice questions.
- `group_accuracy`: original plus semantic reconstruction, or original plus
  semantic plus context reconstruction.

`write_codalab_submission` preserves the notebook submission format: one integer
prediction per line, in test-set order.
