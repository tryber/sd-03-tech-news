from tech_news.database import search_news
import re


def search_by_title(title):
    db_search = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )

    data_list = [(data["title"], data["url"]) for data in db_search]

    return data_list


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
