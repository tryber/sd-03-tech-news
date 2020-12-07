import csv
import os


def formartData(data):
    news = []
    for new in data:
        news.append({
            "url": new[0],
            "title": new[1],
            "timestamp": new[2],
            "writer": new[3],
            "shares_count": new[4],
            "comments_count": new[5],
            "summary": new[6],
            "sources": new[7],
            "categories": new[8],
        })
    return news


def csv_importer(filepath):
    try:
        file_name = os.path.basename(filepath)
        if (not file_name.endswith('.csv')):
            raise ValueError('Formato invalido')
        with open(filepath, 'r') as file:
            file_reader = csv.reader(file, delimiter=';')
            _header, *data = file_reader
            return formartData(data)
    except FileNotFoundError:
        raise ValueError(f'Arquivo {file_name} não encontrado')
    else:
        print('ok')
