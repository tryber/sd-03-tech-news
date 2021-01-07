import sys
from tech_news.database import create_news
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import fetch_content, scrape


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
        return create_news(news)
    elif choice == "2":
        path = input("Digite o nome do arquivo CSV a ser exportado:")
        return csv_exporter(path)
    elif choice == "3":
        pages = input("Digite a quantidade de páginas a serem raspadas:")
        news = scrape(fetcher=fetch_content, pages=int(pages))
        return create_news(news)
    elif choice == "4":
        sys.stdout.write("Encerrando script\n")
        return
    else:
        sys.stderr.write("Opção inválida\n")
        return


def analyzer_menu():
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    collector_menu()
