#!/bin/bash

echo "=== SEO Article Agent — Starter ==="

# Step 1: Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Step 2: Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Step 3: Install dependencies
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies..."
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "requirements.txt not found!"
  exit 1
fi

# Step 4: Run FastAPI server with Uvicorn
echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
