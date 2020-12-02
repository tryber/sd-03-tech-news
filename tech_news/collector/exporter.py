import csv
from tech_news.database import find_news

spected_headers = [
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


def filepath_if_is_valid(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    return filepath.split("/")[-1]


def csv_exporter(filepath):
    filepath_if_is_valid(filepath)

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(spected_headers)
        for document in find_news():
            data = [
                document["url"],
                document["title"],
                document["timestamp"],
                document["writer"],
                str(document["shares_count"]),
                str(document["comments_count"]),
                document["summary"],
                ",".join(document["sources"]),
                ",".join(document["categories"]),
            ]
            writer.writerow(data)
