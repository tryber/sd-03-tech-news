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
    writer = selector.css(".tec--author__info__link::text").get()[1:-1]
    return writer


def get_shares_counter(selector):
    shares = (
        selector.css(".tec--toolbar__item::text")
        .get()
        .replace(" ", "")
        .replace("Compartilharam", "")
    )
    return int(shares)


def get_comments_count(selector):
    comments = selector.css(
        ".tec--toolbar__item button::attr(data-count)"
    ).get()
    return int(comments)


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
                Selector(text=source).css(".tec--badge::text").get()[1:-1]
            )
    return sources


def get_categories(selector):
    raw_categories = selector.css('#js-categories a::text').getall()
    categories = []
    for categorie in raw_categories:
        categories.append(categorie[1:-1])
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
    url = f"https://www.tecmundo.com.br/novidades?page={pages}"
    res = fetch_content(url)
    news_selector = Selector(text=res)
    news = news_selector.css(".tec--card__title__link::attr(href)").getall()
    # for new in news:
    # new_info = fetch_content(news[0])
    # get_info_selec = Selector(text=new_info)
    # Chamar as funções pra criar o dicionar passando o seletor pra elas
    return news


if __name__ == "__main__":
    # # print(fetch_content('https://www.tecmundo.com.br/novidades'))
    # print(fetch_content('https://httpbin.org/delay/1'))
    # print(fetch_content('https://httpbin.org/delay/10'))
    # print(scrape(fetch_content, 1))
    url = "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
    print(mount_new(fetch_content, url))
