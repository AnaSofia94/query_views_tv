from fastapi import APIRouter
from .upload import router as upload_router
from .analyze import router as analyze_router
from .query import router as query_router

router = APIRouter()
router.include_router(upload_router)
router.include_router(analyze_router)
router.include_router(query_router)