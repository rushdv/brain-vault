# Setup Guide - Brain Vault

## Prerequisites
- Node.js 18+ (for frontend)
- Python 3.9+ (for backend)
- Git

## Frontend Setup

### Installation
```bash
cd frontend
npm install
```

### Development
```bash
npm run dev
```
The frontend will be available at `http://localhost:5173`

### Build
```bash
npm run build
```

### Linting
```bash
npm run lint
```

## Backend Setup

### Installation
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Development
```bash
cd backend
uvicorn app.main:app --reload
```
The backend API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Environment Variables

Create a `.env` file in the backend directory:
```
ENVIRONMENT=development
DEBUG=true
```

## Running Both Services

### Option 1: Separate Terminals
Terminal 1:
```bash
cd frontend && npm run dev
```

Terminal 2:
```bash
cd backend && uvicorn app.main:app --reload
```

### Option 2: Using Docker (if available)
```bash
docker-compose up
```

## Troubleshooting

### Frontend Issues
- Clear node_modules: `rm -rf node_modules && npm install`
- Clear cache: `npm cache clean --force`

### Backend Issues
- Recreate venv: `rm -rf venv && python -m venv venv`
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## Next Steps
- Read [API.md](./API.md) for API documentation
- Check [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution guidelines
