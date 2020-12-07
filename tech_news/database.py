from pymongo import MongoClient
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def create_news(data):
    db.news.insert_many(data)


def insert_or_update(notice):
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    return list(db.news.find({}, {"_id": False}))


def search_news(query):
    return list(db.news.find(query))


def search_using_title(term):
    return list(db.news.find(
        # {"title": {"$regex": f"^{term}$"}}, {"title": 1, "url": 1, "id": 0}
        {"$regex": re.compile(term, re.IGNORECASE)}
    ))


def search_using_date(term):
    return list(db.news.find(
        {"timestamp": {"$regex": term}}, {"title": 1, "url": 1, "id": 0}
    ))


def search_using_source(term):
    return list(db.news.find(
        {"sources": {"$all": [term]}}, {"title": 1, "url": 1, "id": 0}
    ))


def search_using_categories(term):
    return list(db.news.find(
        {"categories": {"$all": [term]}}, {"title": 1, "url": 1, "id": 0}
    ))


def get_top_news_by_shares():
    return list(db.news.find({}, {"title": 1, "url": 1, "id": 0}).sort(
        {"shares_count": 1}, {"title": 1},
    ).limit(5))


def get_top_news_by_comments():
    return list(db.news.find({}, {"title": 1, "url": 1, "id": 0}).sort(
        {"comments_count": 1}, {"title": 1},
    ).limit(5))
