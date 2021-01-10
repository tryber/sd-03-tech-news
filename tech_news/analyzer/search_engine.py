import re
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
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
