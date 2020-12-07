from tech_news.database import search_news
from datetime import datetime
import re


def search_by_title(title):
    dbValues = search_news({"title": {
        "$regex": f"^{title}$", "$options": "-i"
      }
    })
    if dbValues == []:
        return []
    return[(dbValues[0]["title"], dbValues[0]["url"])]


def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    dbValues = search_news({"timestamp": {"$regex": date}})
    if dbValues == []:
        return []
    return[(dbValues[0]["title"], dbValues[0]["url"])]


def search_by_source(source):
    dbValues = search_news({"sources": {
        "$all": [re.compile(source, re.IGNORECASE)]
    }})
    if dbValues == []:
        return []
    return[(dbValues[0]["title"], dbValues[0]["url"])]


def search_by_category(category):
    dbValues = search_news({"categories": {
        "$all": [re.compile(category, re.IGNORECASE)]
    }})
    if dbValues == []:
        return []
    return[(dbValues[0]["title"], dbValues[0]["url"])]
