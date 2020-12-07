import csv
# from os import path
from tech_news.database import create_news
# csv_importer('./samples/data.csv') para testar


def csv_importer(filepath):
    if not filepath.endswith('.csv'):
        raise ValueError('\nFormato invalido')
    # if not path.exists(filepath)
    #     raise ValueError('\nCaminho inválido')

    try:
        news_file = open(filepath, 'r')
    except OSError:
        print('\nArquivo file_not_exist.csv não encontrado')
    else:
        news_reader = csv.reader(news_file, delimiter=";", quotechar='"')
        header, *news_data = news_reader
        # Separação do header do resto do conteúdo do arquivo
        news_dict = []
        for row in news_data:
            news_dict.append({
                header[0]: row[0],
                header[1]: row[1],
                header[2]: row[2],
                header[3]: row[3],
                header[4]: row[4],
                header[5]: row[5],
                header[6]: row[6],
                header[7]: row[7],
                header[8]: row[8],
            })
        create_news(news_dict)
        print(news_dict)
        news_file.close()
