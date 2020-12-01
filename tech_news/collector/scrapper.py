import requests
import time
from parsel import Selector

URL_BASE = "https://www.tecmundo.com.br/novidades"


def sleep(delay):
    time.sleep(delay)


def fetch_content(url, timeout=3, delay=0.5):
    sleep(delay)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return ""
    else:
        return response.text


def get_detail_content(fetcher, url):
    info = {}
    response = fetcher(url=url)
    sel = Selector(response)

    titles = sel.css(".tec--article__header__title::text").get()
    times = sel.css(".tec--timestamp__item time::attr(datetime)").get()
    writer = sel.css(".tec--author__info__link::text").get()
    shares_count = sel.css(".tec--toolbar__item::text").re_first(r"\d+")
    print(shares_count)
    comments_count = sel.css("#js-comments-btn::text").re_first(r"\d+")
    print(comments_count)
    summary = sel.css("div.tec--article__body > p::text").get()
    sources = sel.css(".z--mb-16 a.tec--badge::text").getall()
    categories = sel.css("#js-categories a::text").getall()

    info["url"] = url
    info["title"] = titles
    info["timestamp"] = times
    info["writer"] = writer
    info["shares_count"] = int(shares_count or "0")
    info["comments_count"] = int(comments_count or "0")
    info["summary"] = summary
    info["sources"] = sources
    info["categories"] = categories
    return info


def get_url_list(sel):
    # Cria uma lista com os links de acesso das notícias.
    return sel.css(".tec--list__item .tec--card__title__link::attr(href)").getall()


def mount_information(fetcher, urls_list):
    params_list = []
    for detail_url in urls_list:
        info = get_detail_content(fetcher=fetcher, url=detail_url)
        print("info")
        params_list.append(info)
    return params_list


def scrape(fetcher, pages=1):
    last_url = URL_BASE
    data_list = []
    i = 1

    while i <= pages:
        response = fetcher(last_url)
        sel = Selector(response)

        # Pega a lista de url da página
        list = get_url_list(sel=sel)

        # Depois de criada a lista de urls
        # é percorrido a lista para acessar as páginas
        # e gravado os dados do detalhe da página
        data = mount_information(fetcher=fetcher, urls_list=list)
        data_list.extend(data)

        # Depois de gravar os dados pega a próxima página
        last_url = sel.css(".tec--btn::attr(href)").get()
        print("ultima url", last_url)
        i += 1

    return data_list
