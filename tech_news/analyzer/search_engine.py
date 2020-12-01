import re
from tech_news.database import db


def search_by_title(title):
    """Seu código deve vir aqui"""
    arr = []
    for document in db.news.find(
        {"title": {"$regex": title, "$options": "-i"}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_date(date):
    """Seu código deve vir aqui"""
    match = re.search(
        "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", date
    )
    if not match:
        raise ValueError("Data inválida")
    arr = []
    for document in db.news.aggregate(
        [{"$match": {"timestamp": {"$regex": date}}}]
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_source(source):
    """Seu código deve vir aqui"""
    arr = []
    for document in db.news.find(
        {"sources": {"$elemMatch": {'$regex': source, "$options": "i"}}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_category(category):
    """Seu código deve vir aqui"""
    arr = []
    for document in db.news.find(
        {"categories": {"$elemMatch": {'$regex': category, "$options": "i"}}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr
