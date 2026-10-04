@echo off
echo ========================================================
echo Starting EcoSense AI Backend (FastAPI + ML Engine)...
echo ========================================================
set PYTHONPATH=%~dp0backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
pause
