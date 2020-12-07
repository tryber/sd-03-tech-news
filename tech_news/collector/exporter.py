import csv
from tech_news.database import find_news

header = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories"
    ]


def csv_exporter(filepath):
    if filepath.endswith('.json'):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        news = find_news()
        for new_news in news:
            writer.writerow(header)
            writer.writerow([
                new_news[header[0]],
                new_news[header[1]],
                new_news[header[2]],
                new_news[header[3]],
                new_news[header[4]],
                new_news[header[5]],
                new_news[header[6]],
                ','.join(new_news[header[7]]),
                ','.join(new_news[header[8]]),
            ])
