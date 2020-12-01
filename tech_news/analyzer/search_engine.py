from tech_news.database import search_news
import re


def search_by_title(title):
    db_search_results = search_news({"title": title}) or []
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples


def search_by_date(date):
    reg_exp = bool(
        re.match("^\\d{4}\\-(0[1-9]|1[012])\\-(0[1-9]|[12][0-9]|3[01])$", date)
    )

    if reg_exp is False:
        return print("Data inválida")

    db_search_results = search_news({"timestamp": {"$regex": date}}) or []
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples


def search_by_source(source):
    db_search_results = search_news({"sources": {"$all": [source]}}) or []
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples


def search_by_category(category):
    db_search_results = search_news({"categories": {"$all": [category]}}) or []
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples
