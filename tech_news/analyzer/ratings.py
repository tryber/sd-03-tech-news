import tech_news.database as db


def top_5_news():
    result = db.find_news()
    if result == []:
        return result
    return [(result[0]["title"], result[0]["url"])]


def top_5_categories():
    result = db.find_news()
    if result == []:
        return result
    return [(result)]
