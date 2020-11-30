import requests
import time
from parsel import Selector


# def fetch_content(url, timeout=3, delay=0.5):
#     """Seu código deve vir aqui"""

def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    try:
        response = requests.get(url, timeout=timeout)
        sleep(delay)
    except requests.ReadTimeout:
        return ''
    else:
        if response.status_code != 200:
            return ''
        else:
            return response.text

arr = []


def scrape(fetcher, pages=1):
    for i in range(pages):
        page = requests.get(
            f"https://www.tecmundo.com.br/novidades?page={i + 1}"
        )
        selector = Selector(text=page.text)
        links = selector.css(".tec--card__title__link::attr(href)").getall()
        for link in links:
            try:
                second_response = requests.get(link)
                infos = Selector(text=second_response.text)
                title = infos.css(".tec--article__header__title::text").get()
                timestamp = infos.css(
                    ".tec--timestamp__item time::attr(datetime)"
                ).get()
                writer = infos.css(".tec--author__info__link::text").get()
                shares_count = infos.css(".tec--toolbar__item::text").get()
                suffix = " Compartilharam"
                if shares_count.endswith(suffix):
                    shares_count = shares_count[: -len(suffix)]
                comments_count = infos.css(".tec--btn::attr(data-count)").get()
                summary = infos.css(".tec--article__body *::text").get()
                print(summary)
                sources = []
                for source in infos.css(
                    ".z--mb-16 .tec--badge::text"
                ).getall():
                    sources.append(source)
                categories = []
                for category in infos.css(
                    ".tec--badge--primary::text"
                ).getall():
                    categories.append(category)
                arr.append(
                    {
                        "url": link,
                        "title": title,
                        "timestamp": timestamp,
                        "writer": writer,
                        "shares_count": shares_count,
                        "comments_count": comments_count,
                        "summary": summary,
                        "sources": sources,
                        "categories": categories,
                    }
                )
            except AttributeError:
                arr.append({'vazio': 0})
    print(arr)


# scrape("https://www.tecmundo.com.br/novidades")

# fetch_content('https://www.tecmundo.com.br/novidades')
# # def scrape(fetcher, pages=1):
# results = []


# def scraper():
#     response = requests.get('https://www.tecmundo.com.br/novidades')
#     selector = Selector(text=response.text)
#     links = selector.css(".tec--card__title__link::attr(href)").getall()
#     for link in links:
#         second_response = requests.get(link)
#         infos = Selector(text=second_response.text)
#         header = infos.css(".tec--article__header__title::text").get()
#         timestamp = infos.css(".tec--timestamp__item time").attrib['datetime']
#         writer = infos.css(".tec--author__info__link::text").get()
#         shares_count = infos.css(".tec--toolbar__item::text").get()
#         comments_count = infos.css(".tec--btn::text").get()
#         summary = infos.css(".tec--article__body p::text").get()
#         print(comments_count)
