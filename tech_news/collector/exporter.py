import csv
from tech_news.database import find_news

# como pego a funçao find_news to database? Preciso criar ela aqui de novo?


def csv_exporter(filepath):
    print(find_news())
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
        list_of_dicts = find_news()
        for dict in list_of_dicts:
            writer.writerow(
                [
                    dict["url"],
                    dict["title"],
                    dict["timestamp"],
                    dict["writer"],
                    dict["shares_count"],
                    dict["comments_count"],
                    dict["summary"],
                    ','.join(dict["sources"]),
                    ','.join(dict["categories"]),
                ]
            )


csv_exporter('test.csv')
