import re
import datetime
from tech_news.database import search_news


def search_by_title(title):
    search_results = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for news in data:
        search_results.append((news["title"], news["url"]))
    return search_results


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        search_results = []
        data = search_news({"timestamp": {"$regex": date}})
        for news in data:
            search_results.append((news["title"], news["url"]))
        return search_results


def search_by_source(source):
    search_results = []
    data = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )
    for news in data:
        search_results.append((news["title"], news["url"]))
    return search_results


def search_by_category(category):
    search_results = []
    data = search_news(
        {"categories": {"$all": [re.compile(category, re.IGNORECASE)]}}
    )
    for news in data:
        search_results.append((news["title"], news["url"]))
    return search_results
