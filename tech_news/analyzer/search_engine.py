import time
import re
from tech_news.database import search_news


def search_by_title(title):
    db_search_results = (
        search_news({"title": {"$regex": re.compile(title, re.IGNORECASE)}})
        or []
    )
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples


def search_by_date(date):
    try:
        time.strftime(date, "%Y-%m-%d")
    except ValueError:
        raise(ValueError("Data inválida"))
    else:
        news = search_using_date(date)
    finally:
        return news


def search_by_source(source):
    db_search_results = (
        search_news({"sources":  {"$all": [re.compile(source, re.IGNORECASE)]}})
        or []
    )
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples


def search_by_category(category):
    db_search_results = (
        search_news({"categories":  {
            "$all": [re.compile(category, re.IGNORECASE)]
            }})
        or []
    )
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples
