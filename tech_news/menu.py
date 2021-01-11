import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.database import create_news


def option_1():
    file = input("Digite o nome do arquivo CSV a ser importado: ")
    imported = csv_importer(file)
    return create_news(imported)


def option_2():
    file = input("Digite o nome do arquivo CSV a ser exportado: ")
    return csv_exporter(file)


def option_3():
    pages = input("Digite a quantidade de páginas a serem raspadas: ")
    scraped = scrape(fetcher=fetch_content, pages=int(pages))
    return create_news(scraped)


def option_4():
    return print("Encerrando script")


def collector_menu():
    generate_menu = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Importar notícias a partir de um arquivo CSV;\n "
        + "2 - Exportar notícias para CSV;\n "
        + "3 - Raspar notícias online;\n "
        + "4 - Sair.\n "
    )

    menu_options = {
        "1": option_1,
        "2": option_2,
        "3": option_3,
        "4": option_4,
    }

    try:
        return menu_options[generate_menu]()
    except KeyError:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
