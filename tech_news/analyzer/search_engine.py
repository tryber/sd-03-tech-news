from tech_news.database import search_news
import datetime


def search_by_title(title):
    arr = []
    for document in search_news(
        {'title': {'$regex': title, '$options': 'i'}}
    ):
        arr.append((document['title'], document['url']))
    return arr


def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')
    else:
        arr = []
        for document in search_news(
            {'timestamp': {'$regex': date}}
        ):
            arr.append((document['title'], document['url']))
    return arr


def search_by_source(source):
    arr = []
    for document in search_news(
        {'sources': {'$elemMatch': {'$regex': source, '$options': 'i'}}}
    ):
        arr.append((document['title'], document['url']))
    return arr


def search_by_category(category):
    arr = []
    for document in search_news(
        {'categories': {'$elemMatch': {'$regex': category, '$options': 'i'}}}
    ):
        arr.append((document['title'], document['url']))
    return arr
