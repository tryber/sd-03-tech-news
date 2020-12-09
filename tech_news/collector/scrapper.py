from time import sleep
from parsel import Selector
import requests


def get_title(selector):
    new = (
        selector.css(".tec--article__header__title")
        .get()
        .replace(
            '<h1 class="tec--article__header__title" id="js-article-title">',
            "",
        )
        .replace("</h1>", "")
    )
    return new

# def get_timestamp(text):
# def get_writer(text):
# def get_shares_count(text):
# def get_comments_count(text):
# def get_summary(text):
# def get_sources(text):
# def get_categories(text):


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
    response = fetch_content(url)
    get_news_selec = Selector(text=response)
    news = get_news_selec.css(".tec--card__title__link::attr(href)").getall()
    # for new in news:
    #     new_info = fetch_content(new)
    #     get_info_selec = Selector(text=new_info)
    # Chamar as funções pra criar o dicionar passando o seletor pra elas
    return news


if __name__ == "__main__":
    # # print(fetch_content('https://www.tecmundo.com.br/novidades'))
    # print(fetch_content('https://httpbin.org/delay/1'))
    # print(fetch_content('https://httpbin.org/delay/10'))
    # print(scrape(fetch_content, 1))
    print('ok')
