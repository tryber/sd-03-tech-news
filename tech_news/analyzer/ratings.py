from tech_news.database import search_news
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
        "categories": ["PC_1", "Console_1"],
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
        "categories": ["PC_2", "Console_2"],
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
        "categories": ["PC_3", "Console_3"],
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
        "categories": ["PC_4", "Console_4"],
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
        "categories": ["PC_5", "Console_5"],
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
        "categories": ["PC_6", "Console_6"],
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
    all_categories = dict()
    news = search_news({})
    for new in news:
        for categorie in new["categories"]:
            if categorie not in all_categories:
                all_categories[categorie] = 1
            else:
                all_categories[categorie] += 1
    top_categories = sorted([categorie for categorie in all_categories])
    return top_categories[:5]


if __name__ == "__main__":
    pprint(top_5_news())
    pprint(top_5_categories())
