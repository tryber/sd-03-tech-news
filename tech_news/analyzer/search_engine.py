import re
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    # ref.: https://docs.python.org/pt-br/3.8/howto/regex.html
    response = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response]


def search_by_date(date):
    # ref:
    # https://www.programiz.com/python-programming/datetime/strptime
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    response_news = search_news(
        {"timestamp": {"$regex": re.compile(date)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response_news]


def search_by_source(source):
    # Obs.: Código praticamente igual à busca por título
    response = search_news(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response]


def search_by_category(category):
    """Seu código deve vir aqui"""
