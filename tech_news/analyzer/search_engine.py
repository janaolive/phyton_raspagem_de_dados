from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date_parsed = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news_list = search_news({"timestamp": date_parsed})
        return [(news["title"], news["url"]) for news in news_list]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]
