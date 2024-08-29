from fastapi import APIRouter

from . import index, bible


router = APIRouter()
router.include_router(index.router)
router.include_router(bible.router)
