from tech_news.database import db, client

t5news_pipeline = [
    {'$sort': {'shares_count': -1, 'comments_count': -1, 'title': -1}},
    {'$limit': 5}
]

t5cat_pipeline = [
    {'$group': {'_id': '$categories', 'soma_cat': {'$sum': 1}}},
    {'$limit': 5},
    {'$sort': { 'soma_cat': -1 }}
]


def top_5_news():
    results = []
    for news in db.news.aggregate(t5news_pipeline):
        results.append((news['title'], news['url']))
    client.close()
    return results


def top_5_categories():
    results = []
    for news in db.news.aggregate(t5cat_pipeline):
        results.append((news['categories']))
    client.close()
    return results
