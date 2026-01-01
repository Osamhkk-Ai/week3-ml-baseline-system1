# Week 3 — Ship-Ready Baseline ML System (Train + Evaluate + Predict)

This project demonstrates a **simple, reproducible baseline machine learning system**
that takes a feature table and produces trained models, evaluation metrics, and batch predictions.

The focus is on:
- clear, runnable steps
- reproducibility (versioned runs + metadata)
- ease of evaluation for reviewers

---

## Project Structure (high level)

```text
week3-ml-baseline-system1/
├─ data/                 # Processed feature tables
├─ models/               # Trained models and run artifacts
├─ outputs/              # Batch prediction outputs
├─ reports/              # Model card and evaluation summary
├─ src/                  # Core ML pipeline (train / predict)
├─ tests/                # Automated tests
└─ README.md
```

---

## Quickstart (recommended path)

Follow the steps below from top to bottom.  
All commands are copy/paste friendly.

### 1) Clone the repository
```bash
git clone https://github.com/Osamhkk-Ai/week3-ml-baseline-system1.git
cd week3-ml-baseline-system1
```

---

### 2) Create and activate a virtual environment

Create a virtual environment using Python 3.11:
```bash
uv venv -p 3.11
```

Activate the environment:

**Mac / Linux**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\activate
```

---

### 3) Install required packages
```bash
uv sync
```

---

### 4) Create sample data
```bash
uv run ml-baseline make-sample-data
```

This creates a small demo feature table:
```text
data/processed/features.csv
```

---

### 5) Train the model
```bash
uv run ml-baseline train --target is_high_value
```

This step:
- trains a baseline classification model
- saves versioned artifacts under `models/runs/`
- updates `models/registry/latest.txt`

**Note:**  
On small or synthetic datasets, some evaluation metrics (e.g., ROC AUC) may be undefined
if only one class is present in a split.  
This is expected behavior and does not indicate a training failure.

---

### 6) Batch predict (PowerShell)
```powershell
$runId = Get-Content models/registry/latest.txt
uv run ml-baseline predict --run latest --input "models/runs/$runId/tables/holdout_input.csv" --output outputs/holdout_preds.csv
```

Output:
```text
outputs/holdout_preds.csv
```

> Inference inputs must **not** include the target column (`is_high_value`).

---

### 7) Run tests
```bash
uv run pytest
```

All tests must pass before submission.

---

## Outputs and artifacts

After running the pipeline, you should see:

```text
models/runs/<run_id>/
├─ model/
├─ metrics/holdout_metrics.json
├─ schema/input_schema.json
└─ tables/holdout_predictions.csv

outputs/holdout_preds.csv
```

---

## What you submit
- working code (`src/`)
- passing tests (`tests/`)
- filled `reports/model_card.md`
- filled `reports/eval_summary.md`

---

## Project notes
- This repository is intended as a **baseline reference implementation**
- The goal is clarity and reproducibility, not model complexity
- Designed to be easy to review and rerun by evaluators
