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
    """Seu código deve vir aqui"""
