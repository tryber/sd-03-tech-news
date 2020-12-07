from tech_news.database import search_news
from datetime import datetime
import re

def search_by_title(title):
    notices = search_news({
        "title": {'$regex':  f"^{ title }$", "$options": '-i'}
    })
    data = []
    for notice in notices:
        data.append((
            notice['title'],
            notice['url'],
        ))
    return data


def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    notices = search_news({"timestamp": {"$regex": date}})
    data = []
    for notice in notices:
        data.append((
            notice['title'],
            notice['url'],
        ))
    return data


def search_by_source(source):
    notices = search_news({
        "sources": {"$all": [re.compile(source, re.IGNORECASE)]}
    })
    data = []
    for notice in notices:
        data.append((
            notice['title'],
            notice['url'],
        ))
    return data


def search_by_category(category):
    notices = search_news({
        "categories": {"$all": [re.compile(category, re.IGNORECASE)]}
    })
    data = []
    for notice in notices:
        data.append((
            notice['title'],
            notice['url'],
        ))
    return data
