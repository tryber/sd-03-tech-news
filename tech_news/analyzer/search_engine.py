import re
import datetime
from tech_news.database import search_news


def search_by_title(title):
    results = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in data:
        results.append((news["title"], news["url"]))
    return results


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        results = []
        data = search_news({"timestamp": {"$regex": date}})
        for news in data:
            results.append((news["title"], news["url"]))
        return results


def search_by_source(source):
    results = []
    data = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )
    for news in data:
        results.append((news["title"], news["url"]))
    return results


def search_by_category(category):
    results = []
    data = search_news(
        {"categories": {"$all": [re.compile(category, re.IGNORECASE)]}}
    )
    for news in data:
        results.append((news["title"], news["url"]))
    return results
