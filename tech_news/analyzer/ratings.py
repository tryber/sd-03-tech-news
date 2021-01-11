from tech_news.database import search_news_aggregate


def top_5_news():
    tuples_list = []
    news = search_news_aggregate([
        {
            "$addFields": {
                "popularity": {"$add": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}},
        {"$limit": 5},
    ])
    for new in news:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


def top_5_categories():
    categories = search_news_aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ])

    top_categories = [
        category["_id"] for category in categories
    ]

    return top_categories
