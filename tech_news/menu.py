from tech_news.collector.exporter import csv_exporter
from tech_news.collector.importer import csv_importer
from tech_news.collector.scrapper import scrape
from tech_news.collector.scrapper import fetch_content
from tech_news.database import create_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_news
from tech_news.analyzer.ratings import top_5_categories
import sys


def collector_menu():
    selection = input(
        "Selecione uma das opções a seguir:\n "
        "1 - Importar notícias a partir de um arquivo CSV;\n "
        "2 - Exportar notícias para CSV;\n "
        "3 - Raspar notícias online;\n "
        "4 - Sair."
    )
    if selection == "1":
        file = input("Digite o nome do arquivo CSV a ser importado:")
        data = csv_importer(file)
        create_news(data)
    elif selection == "2":
        file = input("Digite o nome do arquivo CSV a ser exportado:")
        csv_exporter(file)
    elif selection == "3":
        n = input("Digite a quantidade de páginas a serem raspadas:")
        data = scrape(fetcher=fetch_content, pages=int(n))
        create_news(data)
    elif selection == "4":
        print("Encerrando script\n")
    else:
        print("Opção inválida", file=sys.stderr)


def search_title():
    title = input("Digite o título:")
    search_by_title(title)


def search_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(date)


def search_source():
    source = input("Digite a fonte:")
    search_by_source(source)


def search_category():
    category = input("Digite a categoria:")
    search_by_category(category)


def search_top_news():
    top_5_news()


def search_top_categories():
    top_5_categories()


def exit():
    print("Encerrando script\n")


options = {
    "1": search_title,
    "2": search_date,
    "3": search_source,
    "4": search_category,
    "5": search_top_news,
    "6": search_top_categories,
    "7": exit,
}


def analyzer_menu():
    selection = input(
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
        options[selection]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)


analyzer_menu()
