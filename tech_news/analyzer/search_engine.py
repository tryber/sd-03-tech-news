from tech_news.database import db, client
import re


def search_by_title(title):
    results = []
    for news in db.news.find({'title': {'$regex': title}}):
        results.append((news['title'], news['url']))
    client.close()
    return results


def search_by_date(date):
    results = []
    if not re.search(
        '^(19[0-9]{2}|2[0-9]{3})-(0[1-9]|1[012])-([123]0|[012][1-9]|31)$',
        date
    ):
        raise Exception('Data inválida')
    for news in db.news.find({'timestamp': {'$regex': date}}):
        results.append((news['title'], news['url']))
    client.close()
    return results


def search_by_source(source):
    results = []
    for news in db.news.find({'sources': {'$regex': source}}):
        results.append((news['title'], news['url']))
    client.close()
    return results


def search_by_category(category):
    results = []
    for news in db.news.find({'categories': {'$regex': category}}):
        results.append((news['title'], news['url']))
    client.close()
    return results
