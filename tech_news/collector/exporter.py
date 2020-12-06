from pathlib import Path
import csv
from tech_news.database import find_news

HEADER = [
    'url',
    'title',
    'timestamp',
    'writer',
    'shares_count',
    'comments_count',
    'summary',
    'sources',
    'categories'
]


def csv_exporter(filepath):
    if not Path(filepath).suffix == ".csv":
        raise ValueError("Extensão inválida")
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(HEADER)
        for news in find_news():
            output = [
                news["url"],
                news["title"],
                news["timestamp"],
                news["writer"],
                str(news["shares_count"]),
                str(news["comments_count"]),
                news["summary"],
                ",".join(news["sources"]),
                ",".join(news["categories"]),
            ]
            writer.writerow(output)
