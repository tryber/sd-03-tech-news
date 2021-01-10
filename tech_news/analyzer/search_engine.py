import re
import datetime
from tech_news.database import search_news


def search_by_title(title):
    try:
        regex = re.compile(title, re.IGNORECASE)
        data = search_news({"title": {"$regex": regex}})
        formated_data = [(doc["title"], doc["url"]) for doc in data]
    except KeyError:
        return []
    else:
        return formated_data


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        regex = re.compile(date, re.IGNORECASE)
        data = search_news({"timestamp": regex})
        formated_data = [(doc["title"], doc["url"]) for doc in data]
    except ValueError:
        raise ValueError("Data inválida")
    except KeyError:
        return []
    else:
        return formated_data


def search_by_source(source):
    try:
        regex = re.compile(source, re.IGNORECASE)
        data = search_news({"sources": {"$all": [regex]}})
        formated_data = [(doc["title"], doc["url"]) for doc in data]
    except KeyError:
        return []
    else:
        return formated_data


def search_by_category(category):
    """Seu código deve vir aqui"""
