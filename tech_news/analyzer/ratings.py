from tech_news.database import aggregate_news


def top_5_news():
    results = aggregate_news([
        {
            "$addFields": {
                "popularity": {"$add": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}},
        {"$limit": 5},
    ])

    data = []

    for news in results:
        data.append((news["title"], news["url"]))

    return data


def top_5_categories():
    results = aggregate_news(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "quantity": {"$sum": 1}}},
            {"$sort": {"quantity": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    data = []

    for news in results:
        data.append((news["_id"]))

    return data
