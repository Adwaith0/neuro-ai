# Quick Start Script for Multiple Disease Prediction Dashboard
# This script helps you start both backend and frontend servers

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Multiple Disease Prediction Dashboard" -ForegroundColor Cyan
Write-Host "Quick Start Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$ROOT = "d:\S7\FProj\Multi Model\multiple-disease-prediction-streamlit-app"

# Function to check if port is in use
function Test-Port {
    param($Port)
    $connection = Test-NetConnection -ComputerName localhost -Port $Port -InformationLevel Quiet -WarningAction SilentlyContinue
    return $connection
}

Write-Host "[1/4] Checking prerequisites..." -ForegroundColor Yellow

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "  ✓ Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "  ✗ Python not found! Please install Python first." -ForegroundColor Red
    exit 1
}

# Check Node/npm
try {
    $nodeVersion = node --version 2>&1
    Write-Host "  ✓ Node found: $nodeVersion" -ForegroundColor Green
}
catch {
    Write-Host "  ✗ Node.js not found! Please install Node.js first." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[2/4] Setting up backend..." -ForegroundColor Yellow

# Setup backend
cd "$ROOT\backend"

if (!(Test-Path ".venv")) {
    Write-Host "  Creating Python virtual environment..." -ForegroundColor Gray
    python -m venv .venv
}

Write-Host "  Activating virtual environment..." -ForegroundColor Gray
& ".\.venv\Scripts\Activate.ps1"

if (!(Test-Path ".venv\Lib\site-packages\flask")) {
    Write-Host "  Installing Python dependencies..." -ForegroundColor Gray
    pip install -r requirements.txt -q
}

Write-Host "  ✓ Backend setup complete" -ForegroundColor Green

Write-Host ""
Write-Host "[3/4] Setting up frontend..." -ForegroundColor Yellow

cd "$ROOT\frontend"

if (!(Test-Path "node_modules")) {
    Write-Host "  Installing npm dependencies (this may take a few minutes)..." -ForegroundColor Gray
    npm install
}

Write-Host "  ✓ Frontend setup complete" -ForegroundColor Green

Write-Host ""
Write-Host "[4/4] Starting servers..." -ForegroundColor Yellow

# Check if ports are available
if (Test-Port 5000) {
    Write-Host "  ⚠ Warning: Port 5000 is already in use!" -ForegroundColor Yellow
    Write-Host "    The backend may fail to start." -ForegroundColor Yellow
}

if (Test-Port 5173) {
    Write-Host "  ⚠ Warning: Port 5173 is in use. Frontend will use next available port." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting servers..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend will start on: http://localhost:5000" -ForegroundColor White
Write-Host "Frontend will start on: http://localhost:5173" -ForegroundColor White
Write-Host ""
Write-Host "Opening two new terminals..." -ForegroundColor Gray
Write-Host "  - Terminal 1: Backend (Flask)" -ForegroundColor Gray
Write-Host "  - Terminal 2: Frontend (Vite)" -ForegroundColor Gray
Write-Host ""

# Start backend in new terminal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ROOT\backend'; .\.venv\Scripts\Activate.ps1; Write-Host 'Starting Flask backend server...' -ForegroundColor Green; python app.py"

# Wait a moment for backend to start
Start-Sleep -Seconds 2

# Start frontend in new terminal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ROOT\frontend'; Write-Host 'Starting Vite frontend server...' -ForegroundColor Green; npm run dev"

Write-Host "Servers are starting in separate terminals!" -ForegroundColor Green
Write-Host ""
Write-Host "Once both servers are running:" -ForegroundColor Cyan
Write-Host "  1. Open your browser" -ForegroundColor White
Write-Host "  2. Navigate to the URL shown in the frontend terminal" -ForegroundColor White
Write-Host "  3. Click Dashboard then Medical Predictors to test predictions" -ForegroundColor White
Write-Host ""
Write-Host "To stop the servers: Close both terminal windows or press Ctrl+C in each" -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to exit this setup window..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
