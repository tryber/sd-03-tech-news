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
    """Seu código deve vir aqui"""
