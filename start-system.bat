@echo off
echo ================================
echo   Starting Healthcare System
echo ================================
echo.

echo [1/3] Starting Backend Server...
cd backend
start "Backend API Server" cmd /k "python main.py"
cd ..

echo [2/3] Waiting for backend to initialize...
timeout /t 5 /nobreak > nul

echo [3/3] Starting Frontend...
cd frontend  
start "Flutter Frontend" cmd /k "flutter run -d web-server --web-port 3000"
cd ..

echo.
echo ================================
echo   SYSTEM STARTED!
echo ================================
echo.
echo Backend API: http://localhost:8000
echo Frontend:    http://localhost:3000
echo.
echo Login with: admin / admin123
echo.
echo To test the patient database connection:
echo 1. Go to http://localhost:3000
echo 2. Login with admin/admin123  
echo 3. Go to "New Patient" tab and add a patient
echo 4. Go to "Returning Patients" tab to see saved patients
echo.
echo Close the backend and frontend windows to stop the system.
echo.
pause