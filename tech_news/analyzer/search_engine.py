from pymongo import MongoClient
from decouple import config
import re
import datetime


DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


""" # para testes locais com usuário e senha
client = MongoClient(
    "mongodb://usuario:senha@localhost:27017/?authMechanism=DEFAULT"
)
db = client.tech_news """

""" requisito 5 """


def search_by_title(title):
    ar = []
    for document in db.news.find(
        {"title": {"$regex": title, "$options": "-i"}}
    ):
        title = document["title"]
        url = document["url"]
        ar.append((title, url))
    return ar


""" requisito 6 """


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError('Data inválida')
    else:
        regex = re.compile(date, re.IGNORECASE)
        with client as session:
            db = session.tech_news
            query = db.news.find(
                {"timestamp": regex},
                {"title": 1, "url": 1, "_id": 0}
            )
            result = [(doc["title"], doc["url"]) for doc in query]
            print(result)
            if not len(result):
                return []
            return result


""" requisito 7 """


def search_by_source(source):
    results = db.news.find(
        {"sources": {"$regex": re.compile(source, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]


""" requisito 8 """


def search_by_category(category):
    results = db.news.find(
        {"categories": {"$regex": re.compile(category, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]
