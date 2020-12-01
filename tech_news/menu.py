from tech_news.collector.exporter import csv_exporter
from tech_news.collector.importer import csv_importer
from tech_news.collector.scrapper import scrape
from tech_news.collector.scrapper import fetch_content
from tech_news.database import create_news
import sys


def collector_menu():
    """Seu código deve vir aqui"""
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


def search_by_title():
    input("Digite o título:")


def search_by_date():
    input("Digite a data no formato aaaa-mm-dd:")


def search_by_source():
    input("Digite a fonte:")


def search_by_category():
    input("Digite a categoria:")


def search_top_news():
    print("teste")


def search_top_categories():
    print("teste")


def exit():
    print("Encerrando script\n")


options = {
    "1": search_by_title,
    "2": search_by_date,
    "3": search_by_source,
    "4": search_by_category,
    "5": search_top_news,
    "6": search_top_categories,
    "7": exit,
}


def analyzer_menu():
    """Seu código deve vir aqui"""
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
