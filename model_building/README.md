# Baseline Logistic Regression Pipeline

Use the `train_baseline.py` script to train a logistic regression baseline pipeline.

Example:

```bash
python model_building/train_baseline.py \
  --data datasets/cleaned_data.csv \
  --target target_column_name \
  --output models/baseline_lr.joblib
```

The script will save a scikit-learn Pipeline including imputation, scaling, and a `LogisticRegression` classifier.
