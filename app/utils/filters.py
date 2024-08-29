import datetime as dt


def check_current_year(year: str):
    now = dt.datetime.now()
    year = now.year
    # year from string '2024'
    page_year = dt.datetime.strptime(str(year), "%Y").year
    if page_year < year:
        return year
    else:
        return page_year


FILTERS = {"check_current_year": check_current_year}
