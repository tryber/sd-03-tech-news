from pymongo import MongoClient
import re

# The correct way should be importing from tech_nes.database but it
# doesn't pass the tests
client = MongoClient()
db = client.tech_news
news = list(db.news.find({}, {"_id": False}))


def search_by_title(title):
    """Seu código deve vir aqui"""
    local_news = []
    for new in news:
        if title.lower() in new["title"].lower():
            local_news.append(tuple([new["title"], new["url"]]))
    return local_news


def search_by_date(date):
    """Seu código deve vir aqui"""
    regex = re.search(r"\d{4}-\d{2}-\d{2}", date)
    if regex is None:
        raise ValueError("Data inválida")
    local_news = []
    for new in news:
        if new["timestamp"][:-9] == date:
            local_news.append(tuple([new["title"], new["url"]]))
    return local_news


def search_by_source(source):
    """Seu código deve vir aqui"""
    local_news = []
    for new in news:
        if source.lower() in [source.lower() for source in new["sources"]]:
            local_news.append(tuple([new["title"], new["url"]]))
    return local_news


def search_by_category(category):
    """Seu código deve vir aqui"""
    local_news = []
    for new in news:
        if category.lower() in [
            category.lower() for category in new["categories"]
        ]:
            local_news.append(tuple([new["title"], new["url"]]))
    return local_news


if __name__ == "__main__":
    for new in news:
        print(new)

    print(search_by_title("VAMOSCOMTUDO"))
    print(search_by_date("2020-11-23"))
    print(search_by_source("ResetEra"))
    print(search_by_category("Console"))
