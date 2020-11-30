# import csv

baseArr = [
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

arr = []
new_source = []
new_category = []


# def csv_importer(filepath):
#     try:
#         if filepath[-4:] != ".csv":
#             raise ValueError("Formato invalido")
#         with open(filepath) as file:
#             result = csv.reader(file, delimiter=";", quotechar='"')
#             header, *data = result
#             header.sort()
#             if header != baseArr:
#                 raise ValueError("Formato invalido aqui")
#             for row in data:
#                 url, title, timestamp, writer, shares_count, comments_count
#  summary, sources, categories = row
#                 arr.append({
#                     "url": url,
#                     "title": title,
#                     "timestamp": timestamp,
#                     "writer": writer,
#                     "shares_count": shares_count,
#                     "comments_count": comments_count,
#                     "summary": summary,
#                     "sources": sources,
#                     "categories": categories
#                 })
#     except FileNotFoundError:
#         (f"Arquivo {filepath} não encontrado")
#     else:
#         return arr


# print(csv_importer('correct.csv'))
