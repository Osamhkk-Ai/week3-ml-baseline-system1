# Model Card — Week 3 Baseline

## Problem
This baseline model predicts whether a **user** is considered a high-value
customer based on aggregated historical order behavior.

- **Predict:** `is_high_value` for one user
- **Decision enabled:** analytical flagging of high-value users
- **Constraints:** CPU-only, offline-first, batch inference

---

## Data (contract)

- **Feature table:** `data/processed/features.csv`
- **Unit of analysis:** one row per user
- **Target column:** `is_high_value`
- **Positive class:** `1` (high-value user)
- **Optional IDs (passthrough):**
  - `user_id`

### Target definition
A user is labeled as high value if:

total_amount ≥ 80

---

## Splits (draft for now)

- **Holdout strategy:** random split
- **Stratification:** by `is_high_value`
- **Leakage risks:**
  - Using future transactions when computing aggregated features
  - Mixing records from the same user across train and test sets

---

## Metrics (draft for now)

- **Primary metric:** Accuracy  
  Selected because this is a simple binary classification task using a
  balanced, synthetic dataset.

- **Baseline:** a majority-class dummy model must be reported.

---

## Shipping

- **Artifacts:**
  - trained model
  - evaluation metrics
  - holdout performance tables
  - environment snapshot

- **Known limitations:**
  - Synthetic data does not represent real user behavior
  - Target definition is threshold-based and simplistic
  - No fairness or bias evaluation

- **Monitoring (sketch):**
  - distribution of `n_orders`
  - distribution of `total_amount`
  - rate of positive predictions (`is_high_value = 1`)
