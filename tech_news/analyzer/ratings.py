def top_5_news():
    """Seu código deve vir aqui"""


def top_5_categories():
    """Seu código deve vir aqui"""
from tech_news.database import db


def top_5_news():
    """Seu código deve vir aqui"""


def top_5_categories():
    top_five = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "quantity": {"$sum": 1}}},
            {"$sort": {"quantity": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )

    for position in top_five:
        return [(position["_id"])]

    return []
