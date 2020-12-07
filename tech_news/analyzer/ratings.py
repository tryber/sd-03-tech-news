from tech_news.database import db, client

t5news_pipeline = [
    {'$addFields': {"interactions": {
        "$add": ["$shares_count", "$comments_count"]
        }
    }},
    {'$sort': {'interactions': -1,'title': 1}},
    {'$limit': 5}
]

t5cat_pipeline = [
    {'$unwind': '$categories'},
    {'$group': {'_id': '$categories', 'soma_cat': {'$sum': 1}}},
    {'$sort': {'soma_cat': -1, '_id': 1}},
    {'$limit': 5}
]


def top_5_news():
    results = []
    for news in db.news.aggregate(t5news_pipeline):
        results.append((news['title'], news['url']))
    client.close()
    return results or []


def top_5_categories():
    # Insere o campo com o nome das categorias no array de resultados.
    # Essa é outra forma de fazer apend em uma lista como na fção anterior
    results = [
        category["_id"] for category in db.news.aggregate(t5cat_pipeline)
    ]
    client.close()
    return results
