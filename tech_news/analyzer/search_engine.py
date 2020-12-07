from tech_news.database import search_news
from datetime import datetime
import re


def search_by_title(title):
    news = search_news({
        "title": {'$regex':  f"^{ title }$", "$options": '-i'}
    })
    data = []
    for new in news:
        data.append((
            new['title'],
            new['url'],
        ))
    return data


def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    news = search_news({"timestamp": {"$regex": date}})
    data = []
    for new in news:
        data.append((
            new['title'],
            new['url'],
        ))
    return data


def search_by_source(source):
    news = search_news({
        "sources": {"$all": [re.compile(source, re.IGNORECASE)]}
    })
    data = []
    for new in news:
        data.append((
            new['title'],
            new['url'],
        ))
    return data


def search_by_category(category):
    news = search_news({
        "categories": {"$all": [re.compile(category, re.IGNORECASE)]}
    })
    data = []
    for new in news:
        data.append((
            new['title'],
            new['url'],
        ))
    return data
