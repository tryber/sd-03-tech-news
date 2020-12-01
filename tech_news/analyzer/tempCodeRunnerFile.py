from pymongo import MongoClient


client = MongoClient(
    "mongodb://root:root@localhost:27017/?authMechanism=DEFAULT"
)
db = client.tech_news


def top_5_news():
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
            {"$limit": 10},
        ]
    ):
        category = element["_id"]
        arr.append(category)   
    return arr


print(top_5_categories())
