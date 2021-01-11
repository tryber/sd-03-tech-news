from tech_news.database import aggregate_news


def top_5_news():
    top_news = aggregate_news(
        [
            {
                "$addFields": {
                    "popularity": {
                        "$add": ["$shares_count", "$comments_count"]
                    }
                }
            },
            {"$sort": {"popularity": -1, "title": 1}},
            {"$limit": 5},
        ]
    )

    data_list = [(data["title"], data["url"]) for data in top_news]

    return data_list


def top_5_categories():
    """Seu código deve vir aqui"""
