import sys
# from tech_news.collector import exporter, importer, scrapper
from tech_news.collector.importer import csv_importer 
from tech_news.collector.exporter import csv_exporter
from tech_news.collector.scrapper import scrape

options = "Selecione uma das opções a seguir:\n 1 - Importar notícias a partir de um arquivo CSV;\n 2 - Exportar notícias para CSV;\n 3 - Raspar notícias online;\n 4 - Sair."

next_step = {
    '1': 'Digite o nome do arquivo CSV a ser importado:',
    '2': 'Digite o nome do arquivo CSV a ser exportado',
    '3': 'Digite a quantidade de páginas a serem raspadas:',
}

module_to_use = {
    '1': lambda path: csv_importer(path),
    '2': lambda path: csv_exporter(),
    '3': lambda: scrape()
}


def collector_menu():
    try:
        print(options)
        choice = input()
        if choice in next_step.keys():
            print(next_step[choice])
            path = input()
            result = module_to_use[choice](path)
            print(result)
        else:
            print("Opção inválida", file=sys.stderr)
    except (KeyError, TypeError):
        raise ValueError("Opção inválida\n")
    finally:
        print("Encerrando script\n")

# collector_menu()


def analyzer_menu():
 """ssas"""