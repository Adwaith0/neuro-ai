# Backend Prediction Server (Flask API)

Flask REST API server that loads pre-trained ML models and provides prediction endpoints for the frontend application.

## 🚀 Quick Start

### Windows PowerShell:

```powershell
# One-line setup and run
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
```

### Step-by-Step:

```powershell
# 1. Create virtual environment (first time only)
python -m venv .venv

# 2. Activate virtual environment
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies (first time only)
pip install -r requirements.txt

# 4. Start server
python app.py
```

## 🌐 Server Info

- **URL:** `http://localhost:5000`
- **CORS:** Enabled for frontend (`http://localhost:5173`)
- **Models Path:** `../models/` (relative to backend directory)
- **Data Path:** `../data/` (relative to backend directory)

## 📡 API Endpoints

### 1. Diabetes Prediction

```http
POST /predict/diabetes
Content-Type: application/json

{
  "features": [2, 120, 70, 30, 0, 25.5, 0.5, 30]
}
```

**Response:**

```json
{
  "prediction": 0,
  "message": "No Diabetes"
}
```

### 2. Heart Disease Prediction

```http
POST /predict/heart
Content-Type: application/json

{
  "features": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
}
```

**Response:**

```json
{
  "prediction": 1,
  "message": "Heart Disease Detected"
}
```

### 3. Parkinsons Prediction

```http
POST /predict/parkinsons
Content-Type: application/json

{
  "features": [119.992, 157.302, 74.997, 0.00784, 0.00007, ...]
}
```

**Response:**

```json
{
  "prediction": 1,
  "message": "Parkinsons Disease Detected"
}
```

### 4. Autism Risk Assessment

```http
POST /predict/autism
Content-Type: application/json

Option A - Direct features:
{
  "features": [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 25]
}

Option B - Risk percentage:
{
  "riskPercentage": 42
}
```

**Response:**

```json
{
  "prediction": 1,
  "riskLevel": "Medium",
  "message": "Medium risk detected"
}
```

## 🧪 Testing the API

### Using PowerShell (curl):

```powershell
# Test diabetes endpoint
curl http://localhost:5000/predict/diabetes -Method POST -ContentType "application/json" -Body '{"features": [2, 120, 70, 30, 0, 25.5, 0.5, 30]}'

# Test heart endpoint
curl http://localhost:5000/predict/heart -Method POST -ContentType "application/json" -Body '{"features": [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]}'

# Test autism endpoint
curl http://localhost:5000/predict/autism -Method POST -ContentType "application/json" -Body '{"riskPercentage": 42}'
```

### Using Python (test_api.py):

```powershell
python test_api.py
```

## 📦 Dependencies

- **Flask** 3.1.2 - Web framework
- **Flask-CORS** 5.0.0 - Cross-origin requests
- **scikit-learn** 1.7.2 - ML models
- **pandas** 2.3.0 - Data manipulation
- **numpy** 2.2.3 - Numerical computing

See `requirements.txt` for complete list.

## 🔧 Configuration

### Change Port:

Edit `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Change port here
```

### Update Model Paths:

Models are loaded from `../models/` relative to backend directory:

```python
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAVED = os.path.join(BASE_DIR, "models")
```

### CORS Configuration:

CORS is enabled for localhost development:

```python
CORS(app)  # Allows all origins in debug mode
```

## 🐛 Troubleshooting

### Port Already in Use:

```powershell
# Find and kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module Import Errors:

```powershell
pip install -r requirements.txt --force-reinstall
```

### Virtual Environment Issues:

```powershell
# Enable script execution (admin PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Model File Not Found:

- Ensure models exist in `../models/` directory
- Check paths: `diabetes_model.sav`, `heart_disease_model.sav`, `parkinsons_model.sav`
- Autism model auto-generates if missing

## 📝 Notes

- Server runs in **debug mode** by default (auto-reload on file changes)
- Models are loaded once at startup for better performance
- Autism model trains automatically if not found using `../data/autism.csv`
- All paths updated to use new directory structure (`models/`, `data/`)

## 🔗 Integration with Frontend

Frontend (`http://localhost:5173`) automatically connects to backend:

- Ensure backend is running on port 5000
- Frontend makes POST requests to `/predict/*` endpoints
- Responses are handled by React components

**Start Order:**

1. Start backend first: `python app.py`
2. Then start frontend: `npm run dev` (in frontend directory)
