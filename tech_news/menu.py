import sys
from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_source
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories, top_5_news


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
    if choice == "1":
        path = input("Digite o nome do arquivo CSV a ser importado:")
        news = csv_importer(path)
        create_news(news)
        return news
    elif choice == "2":
        path = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(path)
    elif choice == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        news = scrape(fetcher=fetch_content, pages=int(pages))
        create_news(news)
        return news
    elif choice == "4":
        sys.stdout.write("Encerrando script\n")
        return
    else:
        sys.stderr.write("Opção inválida\n")
        return


def analyzer_menu():
    """Seu código deve vir aqui"""
    choice = input("""Selecione uma das opções a seguir:
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")
    if choice == "1":
        title = input("Digite o título:")
        return search_by_title(title)
    elif choice == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)
    elif choice == "3":
        source = input("Digite a fonte:")
        return search_by_source(source)
    elif choice == "4":
        category = input("Digite a categoria:")
        return search_by_category(category)
    elif choice == "5":
        return top_5_news()
    elif choice == "6":
        return top_5_categories()
    elif choice == "7":
        sys.stdout.write("Encerrando script\n")
        return
    else:
        sys.stderr.write("Opção inválida\n")
        return


if __name__ == "__main__":
    collector_menu()
    analyzer_menu()
