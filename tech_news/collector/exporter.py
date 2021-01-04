import csv
from tech_news.database import find_news


def csv_exporter(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    with open(filepath, "w") as file:
        write_csv = csv.writer(file, delimiter=";", quotechar='"')
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
        for new in find_news():
            print(new)
            url = new["url"]
            title = new["title"]
            timestamp = new["timestamp"]
            writer = new["writer"]
            shares_count = new["shares_count"]
            comments_count = new["comments_count"]
            summary = new["summary"]
            sources = ",".join(new["sources"])
            categories = ",".join(new["categories"])
            row_new = [
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
            write_csv.writerow(row_new)
