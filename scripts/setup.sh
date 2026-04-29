#!/bin/bash

# Brain Vault Setup Script
# This script sets up both frontend and backend for development

set -e

echo "🚀 Brain Vault Setup"
echo "===================="

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Frontend Setup
echo -e "\n${BLUE}Setting up Frontend...${NC}"
cd frontend
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
else
    echo "Frontend dependencies already installed"
fi
cd ..
echo -e "${GREEN}✓ Frontend setup complete${NC}"

# Backend Setup
echo -e "\n${BLUE}Setting up Backend...${NC}"
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing backend dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found"
fi

cd ..
echo -e "${GREEN}✓ Backend setup complete${NC}"

echo -e "\n${GREEN}✅ Setup complete!${NC}"
echo -e "\n${BLUE}Next steps:${NC}"
echo "1. Frontend: cd frontend && npm run dev"
echo "2. Backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo -e "\nFor more details, see docs/SETUP.md"
