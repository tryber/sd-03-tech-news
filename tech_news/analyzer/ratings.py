from tech_news.database import search_news_aggregate


def top_5_news():
    topnews = []
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
        topnews.append((new["title"], new["url"]))
    return topnews


def top_5_categories():
    topcategories = []
    categories = search_news_aggregate([
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ])
    for news in categories:
        topcategories.append((news["_id"]))
    return topcategories
