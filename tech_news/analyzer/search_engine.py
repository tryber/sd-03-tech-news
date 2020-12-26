import tech_news.database as db
from datetime import datetime
import re


def search_by_title(title):
    result = db.search_news({"title": {
                          "$regex": f"^{title}$", "$options": "-i"}
                })
    if result == []:
        return result

    return [(result[0]["title"], result[0]["url"])]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    result = db.search_news({"timestamp": {"$regex": date}})
    if result == []:
        return result
    return [(result[0]["title"], result[0]["url"])]


def search_by_source(source):
    result = db.search_news({"sources": {
        "$all": [re.compile(source, re.IGNORECASE)]
    }})
    if result == []:
        return []
    return [(result[0]["title"], result[0]["url"])]


def search_by_category(category):
    result = db.search_news({"categories": {
        "$all": [re.compile(category, re.IGNORECASE)]
    }})
    if result == []:
        return []
    return [(result[0]["title"], result[0]["url"])]
