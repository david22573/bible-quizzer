from fastapi import APIRouter, Request

from app.context import get_global_context
from app.templates import templates

router = APIRouter()


@router.get("/bible")
async def bible(request: Request):
    ctx = get_global_context(request)
    return templates.TemplateResponse(name="bible.html", context=ctx)
