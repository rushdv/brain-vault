# 🎯 START HERE

Welcome to the reorganized Brain Vault project!

## Quick Start

1. **Run setup:**
   ```bash
   bash scripts/setup.sh
   ```

2. **Start frontend (Terminal 1):**
   ```bash
   cd frontend && npm run dev
   ```

3. **Start backend (Terminal 2):**
   ```bash
   cd backend && source venv/bin/activate && uvicorn app.main:app --reload
   ```

4. **Access:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Documentation

- **QUICK_REFERENCE.md** - Common tasks
- **docs/SETUP.md** - Detailed setup
- **docs/API.md** - API documentation
- **docs/CONTRIBUTING.md** - Contribution guidelines

## Project Structure

```
brain-vault/
├── frontend/          React + Vite app
├── backend/           FastAPI backend
├── docs/              Documentation
├── scripts/           Automation
└── legacy/            Archived files
```

Happy coding! 🚀
