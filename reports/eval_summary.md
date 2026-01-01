# Evaluation Summary — Week 3

## What you trained
- **Model family:** Logistic Regression (binary classification)
- **Preprocessing:** Scikit-learn Pipeline with:
  - Numerical features: median imputation
  - Categorical features: most-frequent imputation + one-hot encoding
- **Key hyperparameters:**
  - `max_iter = 500`
  - Fixed decision threshold = 0.5
  - Random seed = 42

---

## Results

### Baseline metrics (majority-class dummy, holdout)
- ROC AUC: 0.50
- PR AUC: 0.20
- Accuracy: 0.80
- Precision: 0.00
- Recall: 0.00
- F1-score: 0.00

### Holdout metrics (trained model)
- ROC AUC: 1.00
- PR AUC: 1.00
- Accuracy: 1.00
- Precision: 1.00
- Recall: 1.00
- F1-score: 1.00
- Positive rate in holdout: 0.20

### Confidence intervals
- ROC AUC 95% CI: [1.00, 1.00]

---

## Error analysis
- **Worst cases:** no misclassified examples observed on the holdout set
- **Leakage check:** perfect performance suggests potential risk of overly simplistic target definition rather than confirmed leakage
- **Next data fixes to try:** evaluate on larger and noisier datasets, refine target definition beyond a single threshold, and test robustness under distribution shift

---

## Recommendation
**Would you ship this baseline?**  
Yes, but **only as a reference baseline**.

**Rationale:** the model clearly outperforms the baseline and passes all quality gates; however, the synthetic nature of the data and perfect metrics indicate optimistic performance that requires validation on more realistic data before production use.