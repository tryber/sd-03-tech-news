from tech_news.database import search_news_with_aggregate


def top_5_news():
    list_query = [
        {
            "$addFields": {
                "popularity": {"$add": ["$shares_count", "$comments_count"]}
            }
        },
        {"$sort": {"popularity": -1, "title": 1}},
        {"$limit": 5},
    ]

    db_search_results = search_news_with_aggregate(list_query) or []

    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]

    return list_of_tuples


def top_5_categories():
    list_query = [
        {"$unwind": "$categories"},
        {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    db_search_results = search_news_with_aggregate(list_query)

    list_of_top_categories = [
        category["_id"] for category in db_search_results
    ]

    return list_of_top_categories
