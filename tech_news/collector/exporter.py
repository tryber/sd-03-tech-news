import csv
from pymongo import MongoClient
from tech_news.collector.csv_helpers import validate_filepath, EXP_HEADERS


def csv_exporter(filepath):
    validate_filepath(filepath)
    client = MongoClient()
    collection = client.tech_news.news

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(EXP_HEADERS)
        for document in collection.find():
            dict = [
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
            writer.writerow(dict)

    # "url",
    # "title",
    # "timestamp",
    # "writer",
    # "shares_count",
    # "comments_count",
    # "summary",
    # "sources",
    # "categories",
