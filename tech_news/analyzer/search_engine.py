from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    string = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(string)
    if results:
        return [(result["title"], result["url"]) for result in results]
    else:
        return []


# Requisito 8
def search_by_date(date):
    try:

        date_obj = datetime.strptime(
            date, "%Y-%m-%d"
            ).strftime("%d/%m/%Y")

        query = {"timestamp": date_obj}

        results = search_news(query)

        if results:
            return [(result["title"], result["url"])for result in results]
        else:
            return []
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
