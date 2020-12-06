import csv
from tech_news.database import db


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    new_data = []
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath, "w") as detail_csv:
            data_result = csv.DictWriter(detail_csv, delimiter=";")

            for obj in data_result:
                (
                    url,
                    title,
                    timestamp,
                    writer,
                    shares_count,
                    comments_count,
                    summary,
                    sources,
                    categories,
                ) = obj

            new_data.append(

                {
                    "url": url,
                    "title": title,
                    "timestamp": timestamp,
                    "writer": writer,
                    "shares_count": shares_count,
                    "comments_count": comments_count,
                    "summary": summary,
                    "sources": sources,
                    "categories": categories,
                }
            )

    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    else:
        return new_data
