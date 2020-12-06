import re
from tech_news.database import get_news


def search_by_title(title):
    # ref.: https://docs.python.org/pt-br/3.8/howto/regex.html
    response = get_news().find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(news["title"], news["url"]) for news in response]


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
