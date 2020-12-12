from tech_news.database import find_news
import csv


header = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories"
    ]


def csv_exporter(filepath):
    if not filepath.endswith("csv"):
        raise ValueError('Formato invalido')
    data_from_database = find_news()
    with open('export_correct.csv', mode='w') as data_file:
        filewrite = csv.writer(data_file, delimiter=';')   
        filewrite.writerow(header)
        for file in data_from_database:
            url = file["url"]
            title = file["title"]
            timestamp = file["timestamp"]
            writer = file["writer"]
            shares_count = file["shares_count"]
            comments_count = file["comments_count"]
            summary = file["summary"]
            sources = "".join(file["sources"])
            categories = ",".join(file["categories"])
        filewrite.writerow(
            [url,
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
   
