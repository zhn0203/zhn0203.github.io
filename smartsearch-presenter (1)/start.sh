#!/bin/bash

echo "📦 Installing backend dependencies..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "🚀 Starting backend server..."
uvicorn app:app --reload &
cd ..

echo "📦 Installing frontend dependencies..."
cd frontend
npm install

echo "🚀 Starting frontend server..."
npm run dev
