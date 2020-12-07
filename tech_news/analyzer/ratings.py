from tech_news.database import search_news_aggregation


def top_5_news():
    db_search_results = search_news_aggregation([
      {"$addFields": {
        "total": {
          "$add": ["$shares_count", "$comments_count"]
        },
      }},
      {
        "$sort": {
          "total": -1,
          "title": 1,
        }
      },
      {
        "$limit": 5,
      }
    ]) or []
    list_of_tuples = [
        (data["title"], data["url"]) for data in db_search_results
    ]
    return list_of_tuples
    # news = get_top_news_by_shares()
    # return news


def top_5_categories():
    db_search_results = search_news_aggregation([
      {
        "$unwind": "$categories",
      },
      {
        "$group": {
          "_id": "$categories",
          "totalCategories": {
            "$sum": 1,
          }
        },
      },
      {
        "$sort": {
          "totalCategories": -1,
          "_id": 1,
        }
      },
      {
        "$limit": 5,
      }
    ]) or []
    list_of_tuples = [
        data["_id"] for data in db_search_results
    ]
    return list_of_tuples
