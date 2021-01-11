import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")

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
        news = find_news()
        for new in news:
            writer.writerow(
                [
                    new["url"],
                    new["title"],
                    new["timestamp"],
                    new["writer"],
                    new["shares_count"],
                    new["comments_count"],
                    new["summary"],
                    ','.join(new["sources"]),
                    ','.join(new["categories"]),
                ]
            )