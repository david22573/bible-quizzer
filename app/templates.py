from fastapi.templating import Jinja2Templates

from app.utils.filters import FILTERS

templates = Jinja2Templates(directory="templates")
templates.env.filters.update(FILTERS)
