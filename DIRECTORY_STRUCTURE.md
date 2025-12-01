# Project Directory Structure

This document describes the organized structure of the Multiple Disease Prediction System project.

## Directory Layout

```
multiple-disease-prediction-streamlit-app/
├── data/                           # All datasets
│   ├── autism.csv                  # Autism screening dataset
│   ├── diabetes.csv                # Diabetes prediction dataset
│   ├── heart.csv                   # Heart disease prediction dataset
│   └── parkinsons.csv              # Parkinson's disease dataset
│
├── models/                         # Trained machine learning models
│   ├── autism_model.sav            # Random Forest - Autism risk assessment
│   ├── diabetes_model.sav          # SVM - Diabetes prediction
│   ├── heart_disease_model.sav     # Logistic Regression - Heart disease
│   └── parkinsons_model.sav        # SVM - Parkinson's disease
│
├── notebooks/                      # Jupyter notebooks
│   ├── training/                   # Model training notebooks
│   │   ├── diabetes_training.ipynb
│   │   ├── heart_training.ipynb
│   │   └── parkinsons_training.ipynb
│   ├── autism_prediction.ipynb     # Autism model development
│   └── model_evaluation.ipynb      # All models evaluation & metrics
│
├── frontend/                       # React + TypeScript frontend (Vite)
│   ├── src/                        # Source code
│   │   ├── components/             # React components
│   │   ├── pages/                  # Page components
│   │   └── ...
│   ├── public/                     # Static assets
│   ├── package.json                # Node dependencies
│   └── vite.config.ts              # Vite configuration
│
├── backend/                        # Flask REST API backend
│   ├── .venv/                      # Python virtual environment
│   ├── app.py                      # Flask API endpoints
│   ├── test_api.py                 # API testing script
│   ├── requirements.txt            # Backend Python dependencies
│   └── README.md                   # Backend documentation
│
├── app.py                          # Streamlit web application
├── requirements.txt                # Root Python dependencies
├── start.ps1                       # PowerShell startup script
└── README.md                       # Main project documentation
```

## Key Directories

### `/data/`

Contains all CSV datasets used for training and evaluation:

- **autism.csv**: 704 records with A1-A10 scores, age, and demographics
- **diabetes.csv**: Medical metrics for diabetes prediction
- **heart.csv**: Cardiovascular health indicators
- **parkinsons.csv**: Voice measurements for Parkinson's detection

### `/models/`

Stores serialized scikit-learn models (.sav files):

- Models are loaded by both the Streamlit app and Flask backend
- Can be retrained using notebooks in `/notebooks/training/`

### `/notebooks/`

Jupyter notebooks for analysis and training:

- **training/**: Original training notebooks from Google Colab
- **model_evaluation.ipynb**: Comprehensive evaluation with metrics, confusion matrices, and cross-validation
- **autism_prediction.ipynb**: Autism model development and analysis

### `/frontend/`

React + TypeScript SPA with Vite:

- Modern UI with Tailwind CSS and glassmorphism design
- Features: Disease predictions, cognitive games, speech tools, autism assessment
- Communicates with Flask backend via REST API

### `/backend/`

Flask REST API:

- Endpoints for all 4 disease predictions
- Autism risk assessment with 20-question screening
- CORS enabled for frontend communication
- Port: 5000

## Path References

When working with files in code:

**From root directory:**

```python
# Load models
'models/diabetes_model.sav'
'models/heart_disease_model.sav'

# Load data
'data/diabetes.csv'
'data/autism.csv'
```

**From notebooks directory:**

```python
# Load models (use relative path)
'../models/diabetes_model.sav'

# Load data (use relative path)
'../data/diabetes.csv'
```

**From backend directory:**

```python
# Use BASE_DIR to navigate up
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "models", "diabetes_model.sav")
data_path = os.path.join(BASE_DIR, "data", "autism.csv")
```

## Quick Start

1. **Backend**: `cd backend` → activate `.venv` → `python app.py`
2. **Frontend**: `cd frontend` → `npm install` → `npm run dev`
3. **Streamlit**: `streamlit run app.py` (from root)
4. **Notebooks**: Open in Jupyter Lab/VS Code from `/notebooks/` directory

## Removed Items

The following items were removed during reorganization:

- `Pneumonia-detection-using-CNN/` - Unrelated project
- `INTEGRATION_COMPLETE.md`, `SETUP_COMPLETE.md` - Temporary docs
- `AUTISM_ASSESSMENT_IMPROVEMENTS.md` - Merged into README
- `.ipynb_checkpoints/` - Auto-generated cache
- `START_HERE.txt` - Replaced by README
- Empty directories: `dataset/`, `saved_models/`, `colab_files_to_train_models/`, `Autism/`

## Notes

- All paths have been updated in code files to reflect new structure
- Models and data remain intact, only directories were reorganized
- Git history preserved for all moved files
- Virtual environments (`.venv`, `node_modules`) remain in place
