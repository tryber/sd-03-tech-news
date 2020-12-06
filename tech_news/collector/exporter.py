from os import path
import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if path.splitext(filepath)[1] != '.csv':
        raise ValueError('Formato invalido')
    with open(filepath, 'w') as file:
        writer = csv.writer(file, delimiter=';')
        headers = [
            "url",
            "title",
            "timestamp",
            "writer",
            "shares_count",
            "comments_count",
            "summary",
            "sources",
            "categories",
        ]
        writer.writerow(headers)
        for document in find_news():
            document['sources'] = ",".join(document['sources'])
            document['categories'] = ",".join(document['categories'])
            writer.writerow(document.values())
