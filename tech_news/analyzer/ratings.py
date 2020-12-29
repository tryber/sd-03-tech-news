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
    result = client.tech_news.news.aggregate([
      {
        # https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/index.html
        "$unwind": "$categories",
      },
      {
        "$group": {
          "_id": "$categories",
          "allCategories": {
            "$sum": 1,
          }
        },
      },
      {
        "$sort": {
          "allCategories": -1,
          "_id": 1,
        }
      },
      {
        "$limit": 5,
      }
    ]) or []
    result_in_list = [
        item["_id"] for item in result
    ]
    return result_in_list

