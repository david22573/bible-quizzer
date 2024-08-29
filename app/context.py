from fastapi import Request


def load_bible():
    return []


def get_global_context(request: Request):
    routes = [
        (r.path, r.name.capitalize())
        for r in request.app.routes[5:]
        if r.path.count("/") <= 2 and "index" not in r.name
    ]
    return {"request": request, "routes": routes, **CONTEXT}


CONTEXT = {
    "bible": load_bible(),
}
