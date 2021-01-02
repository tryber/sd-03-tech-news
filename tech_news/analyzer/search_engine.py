import re
import datetime
from tech_news.database import db


def search_by_title(title):
    regex = re.compile(title, re.IGNORECASE)
    query = db.news.find({"title": regex}, {"title": 1, "url": 1, "_id": 0})
    result = [(doc["title"], doc["url"]) for doc in query]
    if not len(result):
        return []
    return list(result)


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        regex = re.compile(date, re.IGNORECASE)
        query = db.news.find(
            {"timestamp": regex}, {"title": 1, "url": 1, "_id": 0}
        )
        result = [(doc["title"], doc["url"]) for doc in query]
        print(result)
        if not len(result):
            return []
        return result


def search_by_source(source):
    regex = re.compile(source, re.IGNORECASE)
    unwind = {"$unwind": "$sources"}
    match = {
        "$match": {
            "sources": {
                "$regex": regex,
            }
        }
    }

    print([doc for doc in db.news.find()])
    query = db.news.aggregate([unwind, match])
    result = [(doc["title"], doc["url"]) for doc in query]
    if not len(result):
        return []
    return list(result)


def search_by_category(category):
    """Seu código deve vir aqui"""
    regex = re.compile(category, re.IGNORECASE)
    unwind = {"$unwind": "$categories"}
    match = {
        "$match": {
            "categories": {
                "$regex": regex,
            }
        }
    }
    query = db.news.aggregate([unwind, match])
    result = [(doc["title"], doc["url"]) for doc in query]
    if not len(result):
        return []
    return list(result)
