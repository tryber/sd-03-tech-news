from tech_news.database import search_news
import re
import datetime


def search_by_title(title):
    db_search = search_news(
        {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    )

    data_list = [(data["title"], data["url"]) for data in db_search]

    return data_list


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        db_search = search_news(
            {"timestamp": {"$regex": re.compile(date)}}
        )
        data_list = [(data["title"], data["url"]) for data in db_search]

        return data_list


def search_by_source(source):
    db_search = search_news(
        {"title": {"$regex": re.compile(source, re.IGNORECASE)}}
    )

    data_list = [(data["title"], data["url"]) for data in db_search]

    return data_list


def search_by_category(category):
    db_search = search_news(
        {"title": {"$regex": re.compile(category, re.IGNORECASE)}}
    )

    data_list = [(data["title"], data["url"]) for data in db_search]

    return data_list
