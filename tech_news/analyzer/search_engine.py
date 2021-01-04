import datetime
import re
from tech_news.database import search_news


def search_by_title(title):
    tuples_list = []
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


# Referência validação de datas:
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        tuples_list = []
        data = search_news({"timestamp": {"$regex": date}})
        for new in data:
            tuples_list.append((new["title"], new["url"]))
        return tuples_list


# Referência utilização de regex - Python:
# https://docs.python.org/pt-br/3.8/howto/regex.html


def search_by_source(source):
    tuples_list = []
    data = search_news(
        {"sources": {"$all": [re.compile(source, re.IGNORECASE)]}}
    )
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list


def search_by_category(category):
    tuples_list = []
    data = search_news(
        {"categories": {"$all": [re.compile(category, re.IGNORECASE)]}}
    )
    for new in data:
        tuples_list.append((new["title"], new["url"]))
    return tuples_list
