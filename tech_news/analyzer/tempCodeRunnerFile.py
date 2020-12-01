from pymongo import MongoClient
import csv
import re

client = MongoClient(
    "mongodb://root:root@localhost:27017/?authMechanism=DEFAULT"
)
db = client.tech_news


def search_by_title(title):
    arr = []
    for document in db.news.find(
        {"title": {"$regex": title, "$options": "-i"}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_date(date):
    match = re.search("^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", date)
    if not match:
        raise ValueError("Formato invalido")
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


def search_by_category(category):
    """Seu código deve vir aqui"""



search_by_date("23-11-2023")
