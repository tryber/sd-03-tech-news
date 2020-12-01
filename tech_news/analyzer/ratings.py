from tech_news.database import db


def top_5_news():
    """Seu código deve vir aqui"""
    arr = []
    for element in db.news.aggregate(
        [
            {
                "$addFields": {
                    "total": {"$add": ["$shares_count", "$comments_count"]}
                },
            },
            {
                "$sort": {"total": -1, "title": 1},
            },
            {
                "$limit": 5,
            },
        ]
    ):
        title = element["title"]
        url = element["url"]
        arr.append((title, url))
    return arr


def top_5_categories():
    """Seu código deve vir aqui"""
    arr = []
    for element in db.news.aggregate(
        [
            {
                "$unwind": "$categories",
            },
            {
                "$group": {
                    "_id": "$categories",
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    ):
        category = element["_id"]
        arr.append(category)
    return arr
