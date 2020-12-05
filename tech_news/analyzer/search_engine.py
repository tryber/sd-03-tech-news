from datetime import datetime
from tech_news.database import db
from re import IGNORECASE, compile


def find_by_news(pay):
    find_news = db.news.find(
        {"title": {"$regex": compile(pay, IGNORECASE)}},
        {"title": True, "url": True}
    )

    return find_news


def search_by_title(title):
    result = find_by_news(title)

    for new in result:
        return [(new["title"], new["url"])]

    return []


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    find_by_date = db.news.find(
        {"timestamp": {"$regex": compile(date)}},
        {"title": True, "url": True}
    )

    for new in find_by_date:
        return [(new["title"], new["url"])]

    return []


def search_by_source(source):
    result = find_by_news(source)
    print("cheguei", result)

    for new in result:
        return [(new["title"], new["url"])]

    return []


def search_by_category(category):
    result = find_by_news(category)

    for new in result:
        return [(new["title"], new["url"])]

    return []
