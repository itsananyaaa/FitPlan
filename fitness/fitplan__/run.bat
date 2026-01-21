@echo off
REM ========================================================================
REM AI Fitness Planner - Setup & Run Script for Windows
REM ========================================================================

echo.
echo ======================================================================
echo 🏋️ AI Fitness Planner - Setup & Run
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python found
python --version

REM Install dependencies
echo.
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✓ Dependencies installed successfully

REM Ask user what to run
echo.
echo ======================================================================
echo Choose what to run:
echo ======================================================================
echo 1. Run Backend API (Flask)
echo 2. Run Frontend App (Streamlit)
echo 3. Run Both (Backend + Frontend in separate windows)
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Flask Backend API on http://localhost:5000
    echo.
    python run_backend.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Streamlit Frontend on http://localhost:8501
    echo.
    streamlit run app.py
) else if "%choice%"=="3" (
    echo.
    echo Starting both Backend and Frontend...
    echo.
    echo [1] Starting Flask Backend API on http://localhost:5000
    start cmd /k "python run_backend.py"
    
    echo [2] Waiting 3 seconds for backend to start...
    timeout /t 3
    
    echo [3] Starting Streamlit Frontend on http://localhost:8501
    start cmd /k "streamlit run app.py"
    
    echo.
    echo ✓ Both applications are starting in separate windows
    echo.
    echo Frontend: http://localhost:8501
    echo Backend:  http://localhost:5000
    echo.
    echo Press any key in this window to exit...
    pause
) else (
    echo Exiting...
    exit /b 0
)

pause
