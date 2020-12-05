import re
from tech_news.database import db


def search_by_title(title):
    news_list = db.news.find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True}
    )

    for new in news_list:
        return [(new["title"], new["url"])]

    return []


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
