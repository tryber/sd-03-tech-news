from pymongo import MongoClient
import csv

client = MongoClient()
db = client.tech_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writeCsv = csv.writer(file, delimiter=";")
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
        writeCsv.writerow(headers)
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
            writeCsv.writerow(
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


csv_exporter("news.csv")
