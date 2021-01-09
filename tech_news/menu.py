import sys
from tech_news.collector.importer import csv_importer
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape, fetch_content


def create_news(data):
    return print(data)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def option_handler(option):
    def import_csv():
        print("Digite o nome do arquivo CSV a ser importado:")
        filepath = input()
        return create_news(csv_importer(filepath))

    def export_csv():
        print("Digite o nome do arquivo CSV a ser exportado:")
        filepath = input()
        return csv_exporter(filepath)

    def to_scrap():
        print("Digite a quantidade de páginas a serem raspadas:")
        pages = int(input())
        return create_news(scrape(fetcher=fetch_content, pages=pages))

    def to_quit():
        return print('Encerrando script\n')

    OPTIONS = {
        '1': import_csv,
        '2': export_csv,
        '3': to_scrap,
        '4': to_quit
    }

    return OPTIONS[option]()


def collector_menu():
    try:
        print("Selecione uma das opções a seguir:\n 1 - Importar notícias a partir de um arquivo CSV;\n 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;\n 4 - Sair.")
        option = input()
        option_handler(option)
    except KeyError:
        return eprint('Opção inválida')


def analyzer_menu():
    """Seu código deve vir aqui"""

