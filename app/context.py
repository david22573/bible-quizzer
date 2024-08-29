from fastapi import Request


def load_bible():
    return []


def get_global_context(request: Request):
    routes = [(r.path, r.name.capitalize()) for r in request.app.routes[-1:-4:-1]]
    return {"request": request, "routes": routes, **CONTEXT}


CONTEXT = {
    "bible": load_bible(),
}
