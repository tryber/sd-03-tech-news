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
from tech_news.analyzer.ratings import top_5_categories, top_5_news


def import_csv():
    path = input("Digite o nome do arquivo CSV a ser importado:")
    news = csv_importer(path)
    create_news(news)
    return news


def export_csv():
    path = input("Digite o nome do arquivo CSV a ser exportado:")
    return csv_exporter(path)


def scrape_news():
    pages = input("Digite a quantidade de páginas a serem raspadas:")
    news = scrape(fetcher=fetch_content, pages=int(pages))
    create_news(news)
    return news


def exit_menu():
    sys.stdout.write("Encerrando script\n")
    return


def collector_menu():
    """Seu código deve vir aqui"""
    choice = input(
        """Selecione uma das opções a seguir:
 1 - Importar notícias a partir de um arquivo CSV;
 2 - Exportar notícias para CSV;
 3 - Raspar notícias online;
 4 - Sair.
"""
    )
    choices = {
        "1": import_csv,
        "2": export_csv,
        "3": scrape_news,
        "4": exit_menu,
    }
    try:
        choices[choice]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")


def search_title():
    title = input("Digite o título:")
    return search_by_title(title)


def search_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def search_source():
    source = input("Digite a fonte:")
    return search_by_source(source)


def search_category():
    category = input("Digite a categoria:")
    return search_by_category(category)


def analyzer_menu():
    """Seu código deve vir aqui"""
    choice = input(
        """Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )
    choices = {
        "1": search_title,
        "2": search_date,
        "3": search_source,
        "4": search_category,
        "5": top_5_news,
        "6": top_5_categories,
        "7": exit_menu,
    }
    try:
        return choices[choice]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")


if __name__ == "__main__":
    collector_menu()
    analyzer_menu()
