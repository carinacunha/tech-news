from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
