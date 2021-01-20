from database import search_news
from database import db


def top_5_news():
    try:
        data = search_news({})
        ratings = map(
            lambda doc: dict(
                doc, ratings=doc["shares_count"] + doc["comments_count"]
                ), data)
        ratings = sorted(ratings, key=lambda key: key["ratings"])[:5]
        formated_data = [(doc["title"], doc["url"]) for doc in ratings]
    except KeyError:
        return []
    else:
        return formated_data


def top_5_categories():
    try:
        data = db.news.aggregate(
            [
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
                {"$sort": {"_id": 1}}
            ]
        )
        data = [doc["_id"] for doc in sorted(
            [document for document in data], key=lambda key: key["total"])[:5]]
    except KeyError:
        return []
    else:
        return data
