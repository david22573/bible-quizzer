from fastapi import APIRouter, Request

from app.context import get_global_context
from app.templates import templates

router = APIRouter(
    prefix="/bible",
)


@router.get("/", name="bible")
async def index(request: Request):
    ctx = get_global_context(request)
    ctx["bible"] = {"testaments": {"old": {"genesis", 51}, "new": []}}
    return templates.TemplateResponse(name="bible/index.html", context=ctx)


@router.get("/book/{book}/{id}", name="bible.book")
async def book(request: Request, book: str, id: int):
    ctx = get_global_context(request)
    ctx["book"] = {"id": id, "name": book}
    return templates.TemplateResponse(name="bible/book.html", context=ctx)
