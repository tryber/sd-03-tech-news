from tech_news.database import db


def search_by_title(title):
    new_list = []
    try:
        for new in db.news.find({"title": {"$regex": title}}):
            new_list.append(new)
    except not new_list:
        return []
    else:
        return new_list


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
