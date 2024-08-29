from fastapi import APIRouter

from . import bible, index, study


router = APIRouter()

_routes = [bible, study, index]


for route in _routes:
    router.include_router(route.router)
