from re import compile, IGNORECASE
from datetime import datetime
from tech_news.database import db


def search_by_title(title):
    find_by_title = db.news.find(
        {"title": {"$regex": compile(title, IGNORECASE)}}
    )

    for new in find_by_title:
        return [(new["title"], new["url"])]

    return []


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    find_by_date = db.news.find(
        {"timestamp": {"$regex": compile(date)}}
    )

    for new in find_by_date:
        return [(new["title"], new["url"])]

    return []


def search_by_source(source):
    find_by_source = db.news.find(
        {"sources": {"$regex": compile(source, IGNORECASE)}}
    )

    for new in find_by_source:
        return [(new["title"], new["url"])]

    return []


def search_by_category(category):
    find_by_category = db.news.find(
        {"categories": {"$regex": compile(category, IGNORECASE)}},
    )

    for new in find_by_category:
        return [(new["title"], new["url"])]

    return []
