from tech_news.database import aggregate_filter


def top_5_news():
    top_five = []
    for element in aggregate_filter(
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
        top_five.append((title, url))
    return top_five


def top_5_categories():
    top_five = []
    for element in aggregate_filter(
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
        top_five.append(category)
    return top_five
