import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith('csv'):
        raise(ValueError("Formato invalido"))

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

        mongo_news_list = find_news()
        print(mongo_news_list)

        for news in mongo_news_list:
            row = [
                news["url"],
                news["title"],
                news["timestamp"],
                news["writer"],
                news["shares_count"],
                news["comments_count"],
                news["summary"],
                ",".join(news["sources"]),
                ",".join(news["categories"]),
            ]
            writer.writerow(row)
