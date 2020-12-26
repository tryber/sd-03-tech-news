import tech_news.database as db


def top_5_news():
    result = db.find_news()
    if result == []:
        return result


def top_5_categories():
    """Seu código deve vir aqui"""
