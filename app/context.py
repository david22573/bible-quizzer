from fastapi import Request


def load_bible():
    return []


def get_routes(request: Request):
    routes = []
    seen_routes = []
    for r in request.app.routes[5:]:
        route = r.path.split("/")[1]
        route_info = (r.path, route.capitalize())
        if route.strip() and route not in seen_routes:
            seen_routes.append(route)
            routes.append(route_info)
    return routes


def get_global_context(request: Request):
    routes = get_routes(request)
    return {"request": request, "routes": routes, **CONTEXT}


CONTEXT = {
    "bible": load_bible(),
}
