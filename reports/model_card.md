# Model Card — Week 3 Baseline

## Problem
This baseline model predicts whether a **user** is considered a high-value
customer based on aggregated historical order behavior.

- **Target:** `is_high_value` (binary classification)
- **Unit of analysis:** one row per user (aggregated over historical orders)
- **Decision enabled:** analytical flagging of high-value users for downstream actions (e.g., prioritization or retention analysis)
- **Constraints:** CPU-only, offline-first, batch inference

---

## Data (contract)

- **Feature table:** `data/processed/features.csv`
- **Dataset hash (sha256):** `6bda418ff35552e80ee9f66ce1a24c434e51ac59d69d0ff099c68ea623456ebe`
- **Unit of analysis:** one row per user
- **Target column:** `is_high_value`
- **Positive class:** `1` (high-value user)
- **Optional IDs (passthrough):**
  - `user_id`

### Features
- `country` (categorical)
- `n_orders` (int)
- `avg_amount` (float)
- `total_amount` (float)

### Target definition
A user is labeled as high value if:

`total_amount ≥ 80`

---

## Splits

- **Holdout strategy:** random split
- **Test size:** 0.2
- **Stratification:** implicit via classification setup
- **Random seed:** 42
- **Leakage considerations:**
  - Aggregated features must not include future transactions
  - Each user appears in only one split (train or holdout)

---

## Metrics (holdout)

- **Primary metric:** ROC AUC

### Baseline (majority-class dummy)
- ROC AUC: 0.50  
- PR AUC: 0.20  
- Accuracy: 0.80  
- Precision: 0.00  
- Recall: 0.00  
- F1-score: 0.00  

### Trained model (threshold = 0.5)
- ROC AUC: 1.00 (95% CI: [1.00, 1.00])
- PR AUC: 1.00
- Accuracy: 1.00
- Precision: 1.00
- Recall: 1.00
- F1-score: 1.00
- Positive rate in holdout: 0.20

---

## Shipping

- **Artifacts:**
  - trained model (`model.joblib`)
  - input schema
  - holdout metrics
  - holdout prediction tables
  - environment snapshot

---

## Limitations

- The dataset is synthetic and may not reflect real user behavior
- Perfect holdout performance likely indicates an overly separable problem
- No robustness testing on real-world or drifting distributions

---

## Monitoring (sketch)

- Monitor distribution drift for `n_orders` and `total_amount`
- Track positive prediction rate over time
- Recompute evaluation metrics on newly labeled data when available

---

## Reproducibility

- **Run id:** `2026-01-01T16-12-24Z__classification__seed42`
- **Git commit:** recorded in repository history at training time
- **Environment snapshot:**  
  `models/runs/2026-01-01T16-12-24Z__classification__seed42/env/pip_freeze.txt`