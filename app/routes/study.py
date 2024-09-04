from fastapi import APIRouter, Request

from app.context import get_global_context
from app.templates import templates
from app.utils.data import get_books, get_quiz

router = APIRouter(
    prefix="/study",
)


@router.get("/", name="study")
async def index(request: Request):
    ctx = get_global_context(request)
    ctx["books"] = get_books()
    return templates.TemplateResponse(name="study/index.html", context=ctx)


@router.get("/{book}")
async def book(request: Request, book: str):
    ctx = get_global_context(request)
    books = get_books()
    if book not in books:
        return templates.TemplateResponse(name="404.html", context=ctx)
    chapters = books[book]
    ctx.update({"book": book, "chapters": chapters})
    return templates.TemplateResponse(name="study/book.html", context=ctx)


@router.get("/{book}/{chapter}")
async def quiz(request: Request, book: str, chapter: int):
    ctx = get_global_context(request)
    ctx["quiz"] = get_quiz(book, chapter)
    return templates.TemplateResponse(name="study/quiz.html", context=ctx)
