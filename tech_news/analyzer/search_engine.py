from tech_news.database import search_news, get_collection
import re


def search_by_title(title):
    results = get_collection().find(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}},
        {"title": True, "_id": False, "url": True},
    )
    return [(result["title"], result["url"]) for result in results]


def search_by_date(date):
    results = get_collection().find(
        {"date": date}, {"title": True, "_id": False, "url": True}
    )
    return [(result["title"], result["url"]) for result in results]


def search_by_source(source):
    return search_news({"source": {"$match": source}})


def search_by_category(category):
    return search_news({"category": {"$match": category}})
