import csv
from tech_news.database import find_news

HEADER = [
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


def validFile(file):
    if not file.endswith(".csv"):
        raise ValueError("Formato invalido")
    return file.split("/")[-1]


def csv_exporter(filepath):
    validFile(filepath)
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(HEADER)
        for news in find_news():
            var = [
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
            writer.writerow(var)
