from tech_news.database import search_news


def top_5_news():
    """Seu código deve vir aqui"""
    top_news = []
    news = search_news({})
    top_news.append(news)
    return top_news


def top_5_categories():
    """Seu código deve vir aqui"""
    top_categories = []
    news = search_news({})
    top_categories.append(news)
    return top_categories


if __name__ == "__main__":
    print(top_5_news())
