from time import sleep
from parsel import Selector
import requests


def get_title(selector):
    title = selector.css(".tec--article__header__title::text").get()
    return title


def get_timestamp(selector):
    timestamp = selector.css(
        ".tec--timestamp__item time::attr(datetime)"
    ).get()
    return timestamp


def get_writer(selector):
    writer = selector.css(".tec--author__info__link::text").get()
    return writer


def get_shares_counter(selector):
    shares = selector.css(".tec--toolbar__item::text").get()
    if shares is not None:
        shares = shares.replace(" ", "").replace("Compartilharam", "")
        return int(shares)
    return int(0)


def get_comments_count(selector):
    comments = selector.css(
        ".tec--toolbar__item button::attr(data-count)"
    ).get()
    if comments is not None:
        return int(comments)
    return int(0)


def get_summary(selector):
    raw_summary = selector.css(".tec--article__body p *::text").getall()
    summary = "".join(raw_summary)
    return summary


def get_sources(selector):
    raw_sources = selector.css(".tec--badge").getall()
    sources = []
    for source in raw_sources:
        if '"tec--badge"' in source:
            sources.append(
                Selector(text=source).css(".tec--badge::text").get()
            )
    return sources


def get_categories(selector):
    raw_categories = selector.css("#js-categories a::text").getall()
    categories = []
    for categorie in raw_categories:
        categories.append(categorie)
    return categories


def mount_new(fetcher, url):
    new_info = fetcher(url)
    new_selector = Selector(text=new_info)
    temp_new = {"url": url}
    temp_new["title"] = get_title(new_selector)
    temp_new["timestamp"] = get_timestamp(new_selector)
    temp_new["writer"] = get_writer(new_selector)
    temp_new["shares_count"] = get_shares_counter(new_selector)
    temp_new["comments_count"] = get_comments_count(new_selector)
    temp_new["summary"] = get_summary(new_selector)
    temp_new["sources"] = get_sources(new_selector)
    temp_new["categories"] = get_categories(new_selector)
    return temp_new


def fetch_content(url, timeout=3, delay=0.5):
    """Seu código deve vir aqui"""
    sleep(delay)
    try:
        res = requests.get(url, timeout=timeout)
    except requests.ReadTimeout:
        res = ""
    finally:
        if res == "" or res.status_code != 200:
            return ""
        else:
            return res.text


def scrape(fetcher, pages=1):
    """Seu código deve vir aqui"""
    news_links = []
    for page in range(1, pages + 1):
        url = f"https://www.tecmundo.com.br/novidades?page={page}"
        res = fetch_content(url)
        news_selector = Selector(text=res)
        news = news_selector.css(
            "article .tec--card__info h3 a::attr(href)"
        ).getall()
        for new in news:
            news_links.append(new)

    news = []
    for new in news_links:
        temp_new = mount_new(fetch_content, new)
        news.append(temp_new)
    return news


if __name__ == "__main__":
    print(scrape(fetch_content, 2))
