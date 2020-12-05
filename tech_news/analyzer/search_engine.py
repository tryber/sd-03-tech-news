import re
from datetime import datetime
from tech_news.database import db


def search_by_title(title):
    news_list = db.news.find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True}
    )

    for new in news_list:
        return [(new["title"], new["url"])]

    return []


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news_list = db.news.find(
        {"timestamp": {"$regex": re.compile(date)}},
        {"title": True, "_id": False, "url": True}
    )

    for new in news_list:
        return [(new["title"], new["url"])]

    return []


def search_by_source(source):
    news_list = db.news.find(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True}
    )

    for new in news_list:
        return [(new["title"], new["url"])]

    return []


def search_by_category(category):
    news_list = db.news.find(
        {"categories": {"$regex": re.compile(category, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True}
    )

    for new in news_list:
        return [(new["title"], new["url"])]

    return []
