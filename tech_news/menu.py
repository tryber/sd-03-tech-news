# Referência:
# https://github.com/tryber/sd-03-tech-news/blob/jafet6-tech-news/tech_news/menu.py
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


def collector_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Importar notícias a partir de um arquivo CSV;\n "
        + "2 - Exportar notícias para CSV;\n "
        + "3 - Raspar notícias online;\n "
        + "4 - Sair.\n "
    )

    if user_input == "1":
        file = input("Digite o nome do arquivo CSV a ser importado: ")
        imported = csv_importer(file)
        return create_news(imported)
    elif user_input == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado: ")
        return csv_exporter(file)
    elif user_input == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas: ")
        scraped = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(scraped)
    elif user_input == "4":
        return print("Encerrando script")
    else:
        return print("Opção inválida", file=sys.stderr)


def choice_title():
    title = input("Digite o título: ")
    return search_by_title(title)


def choice_date():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(date)


def choice_source():
    source = input("Digite a fonte: ")
    return search_by_source(source)


def choice_category():
    category = input("Digite a categoria: ")
    return search_by_category(category)


def choice_top_news():
    return top_5_news()


def choice_top_categories():
    return top_5_categories()


def choice_exit():
    return print("Encerrando script\n")


def analyzer_menu():
    user_input = input(
        "Selecione uma das opções a seguir:\n "
        + "1 - Buscar notícias por título;\n "
        + "2 - Buscar notícias por data;\n "
        + "3 - Buscar notícias por fonte;\n "
        + "4 - Buscar notícias por categoria;\n "
        + "5 - Listar top 5 notícias;\n "
        + "6 - Listar top 5 categorias;\n "
        + "7 - Sair.\n "
    )

    dict_choice = {
        "1": choice_title,
        "2": choice_date,
        "3": choice_source,
        "4": choice_category,
        "5": choice_top_news,
        "6": choice_top_categories,
        "7": choice_exit,
    }

    try:
        return dict_choice[user_input]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    analyzer_menu()
