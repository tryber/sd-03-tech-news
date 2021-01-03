from tech_news.database import search_news
import re
from datetime import datetime


def search_by_title(title):
    results = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )
    for news in results:
        return [(news["title"], news["url"])]

    return []


def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")

    results = search_news(
        {"timestamp": {"$regex": re.compile(date)}}
    )
    for news in results:
        return [(news["title"], news["url"])]

    return []


def search_by_source(source):
    results = search_news(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}}
    )
    for news in results:
        return [(news["title"], news["url"])]

    return []


def search_by_category(category):
    results = search_news(
        {"categories": {"$regex": re.compile(category, re.IGNORECASE)}}
    )
    for news in results:
        return [(news["title"], news["url"])]

    return []
