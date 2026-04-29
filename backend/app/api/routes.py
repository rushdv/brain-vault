"""API Routes for Brain Vault Backend"""
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["data"])


@router.get("/data")
async def get_data():
    """Get sample data from the backend"""
    return {"message": "Hello from FastAPI Backend!", "status": "success"}
