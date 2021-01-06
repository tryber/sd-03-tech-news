from tech_news.database import search_news
from collections import Counter
from pprint import pprint


TEST_NEWS = [
    {
        "url": "https://www.tecmundo.com.br/noticia_1.htm",
        "title": "noticia_1",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_1",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_1",
        "sources": ["Fonte_1"],
        "categories": ["acao", "comedia"],
    },
    {
        "url": "https://www.tecmundo.com.br/noticia_2.htm",
        "title": "noticia_2",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_2",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_2",
        "sources": ["Fonte_2"],
        "categories": ["acao", "drama"],
    },
    {
        "url": "https://www.tecmundo.com.br/noticia_3.htm",
        "title": "noticia_3",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_3",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_3",
        "sources": ["Fonte_3"],
        "categories": ["aventura", "terror"],
    },
    {
        "url": "https://www.tecmundo.com.br/noticia_4.htm",
        "title": "noticia_4",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_4",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_4",
        "sources": ["Fonte_4"],
        "categories": ["aventura", "2d"],
    },
    {
        "url": "https://www.tecmundo.com.br/noticia_5.htm",
        "title": "noticia_5",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_5",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_5",
        "sources": ["Fonte_5"],
        "categories": ["terror", "simulacao"],
    },
    {
        "url": "https://www.tecmundo.com.br/noticia_6.htm",
        "title": "noticia_6",
        "timestamp": "2020-11-23T11:00:01",
        "writer": "Escritor_6",
        "shares_count": 1,
        "comments_count": 1,
        "summary": "Sumario da noticia_6",
        "sources": ["Fonte_6"],
        "categories": ["terror", "aventura"],
    },
]


def top_5_news():
    """Seu código deve vir aqui"""
    top_news = []
    news = search_news({})
    for new in news:
        top_news.append(
            {
                "title": new["title"],
                "url": new["url"],
                "popularity": new["comments_count"] + new["shares_count"],
            }
        )
    sorted_list = sorted(top_news, key=lambda a: a["popularity"], reverse=True)
    return [(new["title"], new["url"]) for new in sorted_list[:5]]


def top_5_categories():
    """Seu código deve vir aqui"""
    top_categories = []
    news = search_news({})
    for new in news:
        for categorie in new["categories"]:
            top_categories.append(categorie)
    categories_unsorted = Counter(sorted(top_categories))
    top_categories = [key for key, _ in categories_unsorted.most_common()]
    return top_categories[:5]


if __name__ == "__main__":
    pprint(top_5_news())
    pprint(top_5_categories())
