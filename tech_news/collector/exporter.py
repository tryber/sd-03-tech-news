from tech_news.database import db
import csv


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        write_csv = csv.writer(file, delimiter=";")
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
        write_csv.writerow(headers)
        for document in db.news.find({}):
            url = document["url"]
            title = document["title"]
            timestamp = document["timestamp"]
            writer = document["writer"]
            shares_count = document["shares_count"]
            comments_count = document["comments_count"]
            summary = document["summary"]
            sources = "".join(document["sources"])
            categories = ",".join(document["categories"])
            write_csv.writerow(
                [
                    url,
                    title,
                    timestamp,
                    writer,
                    shares_count,
                    comments_count,
                    summary,
                    sources,
                    categories,
                ]
            )
