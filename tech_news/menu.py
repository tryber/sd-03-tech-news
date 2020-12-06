from tech_news.collector import importer, exporter, scrapper
import sys

# User tech-news-collector para executar este programa direto do shell

menu = """Selecione uma das opções a seguir:
1 - Importar notícias a partir de um arquivo CSV;
2 - Exportar notícias para CSV;
3 - Raspar notícias online;
4 - Sair.
"""


def collector_menu():
    user_choice = int(input(menu))
    if user_choice == 1:
        path = input('Digite o nome do arquivo CSV a ser importado:')
        importer.csv_importer(path)
    elif user_choice == 2:
        path = input('Digite o nome do arquivo CSV a ser exportado:')
        exporter.csv_exporter(path)
    elif user_choice == 3:
        pages = input(
            'Digite a quantidade de páginas a serem raspadas:'
            )
        scrapper.scrape(int(pages))
    elif user_choice == 4:
        print('Encerrando script\n')
        exit
    else:
        sys.stderr.write('Opção inválida\n')


def analyzer_menu():
    """Seu código deve vir aqui"""
