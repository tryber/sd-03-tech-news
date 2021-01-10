from tech_news.database import find_news
import csv


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        news_list = find_news()
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
        for news in news_list:
            infos = [
                news["url"],
                news["title"],
                news["timestamp"],
                news["writer"],
                news["shares_count"],
                news["comments_count"],
                news["summary"],
                ','.join(news["sources"]),
                ','.join(news["categories"]),
            ]
            writer.writerow(infos)
