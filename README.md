# Week 3 — Ship-Ready Baseline ML System (Train + Evaluate + Predict)

Turn a feature table into a **reproducible, CPU-friendly ML baseline** with:
- a training command that saves versioned artifacts, and
- a batch prediction command with schema guardrails.

This repo is designed to be:
- **offline-first** (no external services required),
- **reproducible** (run metadata + environment capture),
- **portfolio-ready** (clean structure + model card).

---

## Quickstart

### 1) Setup
```bash
uv sync
```

---

### 2) Create sample data (if needed)
```bash
uv run ml-baseline make-sample-data
```

This writes a small demo feature table to:
- `data/processed/features.csv`

---

### 3) Train a baseline model
```bash
uv run ml-baseline train --target is_high_value
```

Artifacts are written to:
- `models/runs/<run_id>/`
- `models/registry/latest.txt` points to the most recent run

---

### 4) Batch predict
```bash
uv run ml-baseline predict   --run latest   --input models/runs/<run_id>/tables/holdout_input.csv   --output outputs/holdout_preds.csv
```

**Note:** inference inputs must not include the target column (`is_high_value`).

---

### 5) Tests
```bash
uv run pytest
```

All tests must pass before submission.

---

## Artifacts

- Trained model and run metadata:  
  `models/runs/<run_id>/`
- Holdout evaluation metrics:  
  `models/runs/<run_id>/metrics/holdout_metrics.json`
- Input schema (feature contract):  
  `models/runs/<run_id>/schema/input_schema.json`
- Batch predictions:  
  `outputs/holdout_preds.csv`

---

## What you submit
- working code (`src/`)
- passing tests (`tests/`)
- filled `reports/model_card.md`
- filled `reports/eval_summary.md`

---

## Notes
- Training data may include the target column.
- Inference inputs **must not** include the target.
- This system is intended as a baseline reference, not a production model.
