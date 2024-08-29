from fastapi import APIRouter, Request

from app.context import get_global_context
from app.templates import templates

router = APIRouter(
    prefix="/study",
)


@router.get("/", name="study")
async def index(request: Request):
    ctx = get_global_context(request)
    return templates.TemplateResponse(name="study/index.html", context=ctx)
