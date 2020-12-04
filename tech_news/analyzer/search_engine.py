import re
from datetime import datetime
from tech_news.database import get_news


def search_by_title(title):
    response_news = get_news().find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response_news]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    response_news = get_news().find(
        {"timestamp": {"$regex": re.compile(date)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response_news]


def search_by_source(source):
    response_news = get_news().find(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response_news]


def search_by_category(category):
    response_news = get_news().find(
        {"categories": {"$regex": re.compile(category, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response_news]
