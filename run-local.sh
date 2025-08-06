#!/bin/bash

echo "🚀 Starting Test Fullstack App..."
echo ""
echo "Ports:"
echo "- Frontend: http://localhost:3001"
echo "- Backend: http://localhost:8001"
echo ""

# Backend
echo "📦 Starting Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Frontend
echo "🎨 Starting Frontend..."
cd frontend
npm install
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Both services are running!"
echo "Press Ctrl+C to stop both services"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID" INT
wait