from tech_news.database import search_news
from collections import Counter
from pprint import pprint


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
