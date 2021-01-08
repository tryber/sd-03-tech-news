from tech_news.database import search_news


def search_by_title(title):
    query = {
        "title":
            {"$regex": title, "$options": "i"}
        }
    news_list = search_news(query)
    search_results = [(news["title"], news["url"]) for news in news_list]
    return search_results


def search_by_date(date):
    """Seu código deve vir aqui"""


def search_by_source(source):
    """Seu código deve vir aqui"""


def search_by_category(category):
    """Seu código deve vir aqui"""
