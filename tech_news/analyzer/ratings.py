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
    """Seu código deve vir aqui"""
