@echo off
echo === SEO Article Agent — Windows Starter ===

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Starting FastAPI server...
uvicorn app.main:app --reload
