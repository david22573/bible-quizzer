from fastapi import APIRouter, Request

from app.templates import templates
from app.context import get_global_context


router = APIRouter(tags=["Index"])


@router.get("/")
async def home(request: Request):
    ctx = get_global_context(request)
    return templates.TemplateResponse(name="index.html", context=ctx)


@router.get("/about")
async def about(request: Request):
    ctx = get_global_context(request)
    return templates.TemplateResponse(name="about.html", context=ctx)


@router.get("/contact")
async def contact(request: Request):
    ctx = get_global_context(request)
    return templates.TemplateResponse(name="contact.html", context=ctx)
