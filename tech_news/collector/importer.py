import csv
# csv_importer('./samples/data.csv) para testar
# from os import path

def csv_importer(filepath):
    if not filepath.endswith('.csv'):
        print('\nArquIn)v(áliD(etectad)o(')

    try:
        news_file = open(filepath, 'r')
    except OSError:
        print('Erro ao abrir o arquivo', OSError)
    else:
        news_reader = csv.reader(news_file, delimiter=";", quotechar='"')
        header, *news_data = news_reader
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

        print(header, '\nDados prontos:', news_dict)
        news_file.close()
