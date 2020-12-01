import csv

expected_header = [
    "categories",
    "comments_count",
    "shares_count",
    "sources",
    "summary",
    "timestamp",
    "title",
    "url",
    "writer",
]


def append_arr(arr, result):
    header, *data = result
    header.sort()
    if header != expected_header:
        raise ValueError("Formato invalido aqui")
    for row in data:
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
        ) = row

        arr.append(
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


def csv_importer(filepath):
    arr = []
    try:
        if not filepath.endswith(".csv"):
            raise ValueError("Formato invalido")
        with open(filepath) as file:
            result = csv.reader(file, delimiter=";", quotechar='"')
            append_arr(arr, result)
    except FileNotFoundError:
        raise ValueError("Arquivo file_not_exist.csv não encontrado")
    else:
        return arr
