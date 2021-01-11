import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.database import create_news


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


def exit():
    print("Encerrando script\n")


collector_options = {
    "1": importer,
    "2": exporter,
    "3": scraper,
    "4": exit,
}


def collector_menu():
    options = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Importar notícias a partir de um arquivo CSV;\n "
        "2 - Exportar notícias para CSV;\n "
        "3 - Raspar notícias online;\n "
        "4 - Sair."
    )
    try:
        collector_options[options]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)


def opt_title():
    title = input("Digite o título: ")
    return search_by_title(title)


def opt_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(date)


def opt_source():
    source = input("Digite a fonte: ")
    return search_by_source(source)


def opt_category():
    category = input("Digite a categoria: ")
    return search_by_category(category)


def opt_top_news():
    return top_5_news()


def opt_top_categories():
    return top_5_categories()


def opt_exit():
    return print("Encerrando script\n")


def analyzer_menu():
    options = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por fonte;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair.\n "
    )

    analyzer_options = {
        "1": opt_title,
        "2": opt_date,
        "3": opt_source,
        "4": opt_category,
        "5": opt_top_news,
        "6": opt_top_categories,
        "7": opt_exit,
    }

    try:
        return analyzer_options[options]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
