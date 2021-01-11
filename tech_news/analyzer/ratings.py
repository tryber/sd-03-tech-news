from tech_news.database import aggregate_news


def top_5_news():
    topNews = []
    data = aggregate_news([
        {
            "$addFields": {
                "popularity": {"$add": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}},
        {"$limit": 5},
    ])

    for news in data:
        topNews.append((news["title"], news["url"]))

    return topNews


def top_5_categories():
    topCategories = []
    data = aggregate_news(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "quantity": {"$sum": 1}}},
            {"$sort": {"quantity": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )

    for news in data:
        topCategories.append((news["_id"]))

    return topCategories
