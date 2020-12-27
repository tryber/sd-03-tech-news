import tech_news.database as db
from tech_news.database import client


def top_5_news():
    # https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/index.html
    result = client.tech_news.news.aggregate([
      {"$addFields": {
        "total": {
          "$add": ["$shares_count", "$comments_count"]
        },
      }},
      {
        "$limit": 5,
      }
    ]) or []
    result_in_list = [
        (item["title"], item["url"]) for item in result
    ]
    return result_in_list


def top_5_categories():
    result = db.find_news()
    if result == []:
        return result
    return [(result)]
