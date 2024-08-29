from fastapi import Request


def get_global_context(request: Request):
    routes = request.app.routes[4:]
    return {"request": request, "routes": routes, **CONTEXT}


CONTEXT = {}
