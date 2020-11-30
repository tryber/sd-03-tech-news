from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))


def top_5_news():
    """Seu código deve vir aqui"""
    rated = []
    with client as session:
        db = session.tech_news
        docs = db.news.find()
        for doc in docs:
            doc["rating"] = doc["shares_count"] + doc["comments_count"]
            rated.append(doc)
        rated = sorted(rated, key=lambda k: k["rating"])
        rated = [(doc["title"], doc["url"]) for doc in rated]
        rated = rated[:5]
    return rated


def top_5_categories():
    """Seu código deve vir aqui"""
    with client as session:
        db = session.tech_news
        docs = db.news.aggregate([
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ])
        rated = [doc for doc in docs]
        print(rated)
        rated = sorted(rated, key=lambda k: k["total"])
        # rated = sorted(rated, key=lambda k: k["_id"])
        rated = [doc["_id"] for doc in rated]
        rated = rated[:5]
        return rated
