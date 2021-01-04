import sys
from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def importer():
    file = input("Digite o nome do arquivo CSV a ser importado: ")
    data = csv_importer(file)
    create_news(data)


def exporter():
    file = input("Digite o nome do arquivo CSV a ser exportado: ")
    csv_exporter(file)


def scraper():
    pages = input("Digite a quantidade de páginas a serem raspadas: ")
    data = scrape(fetcher=fetch_content, pages=int(pages))
    create_news(data)


def exit_script():
    print("Encerrando script\n")


collector_options = {
    "1": importer,
    "2": exporter,
    "3": scraper,
    "4": exit_script,
}


def collector_menu():
    option = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Importar notícias a partir de um arquivo CSV;\n "
        "2 - Exportar notícias para CSV;\n "
        "3 - Raspar notícias online;\n "
        "4 - Sair."
    )
    try:
        collector_options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)


def search_title():
    title = input("Digite o título: ")
    search = search_by_title(title)
    print(search)


def search_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    search = search_by_date(date)
    print(search)


def search_source():
    source = input("Digite a fonte: ")
    search = search_by_source(source)
    print(search)


def search_category():
    category = input("Digite a categoria: ")
    search = search_by_category(category)
    print(search)


def search_top_news():
    news = top_5_news()
    print(news)


def search_top_categories():
    categories = top_5_categories()
    print(categories)


analyzer_options = {
    "1": search_title,
    "2": search_date,
    "3": search_source,
    "4": search_category,
    "5": search_top_news,
    "6": search_top_categories,
    "7": exit_script,
}


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair."
    )
    try:
        analyzer_options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
