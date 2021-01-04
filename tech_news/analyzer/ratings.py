from tech_news.database import aggregate_news


def top_5_news():
    tuples_list = []
    data = aggregate_news(
        [
            {
                "$addFields": {
                    "popularidade": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                },
            },
            {
                "$sort": {"popularidade": -1, "title": 1},
            },
            {
                "$limit": 5,
            },
        ]
    )
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


def top_5_categories():
    categories_list = []
    data = aggregate_news(
        [
            {"$unwind": "$categories"},
            {
                "$group": {
                    "_id": "$categories",
                    "count": {"$sum": 1},
                }
            },
            {"$sort": {"count": -1, "_id": 1}},
            {"$limit": 5},
        ]
    )
    for new in data:
        categories_list.append(new["_id"])
    return categories_list
