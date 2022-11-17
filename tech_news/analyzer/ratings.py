from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_list = find_news()
    classified_news = sorted(
        news_list, key=lambda news: news["comments_count"], reverse=True
    )
    return [
        (news["title"], news["url"])
        for news in classified_news
        if classified_news.index(news) < 5
    ]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    news_list = find_news()
    categories = {news["category"]: 0 for news in news_list}
    classified_categories = sorted(categories, key=lambda category: category)
    categories = {key: 0 for key in classified_categories}
    for news in news_list:
        categories[news["category"]] += 1
    ordered_categories = sorted(
        categories.items(), key=lambda category: (category[1]), reverse=True
    )
    return [
        category
        for category, qnt in ordered_categories
        if ordered_categories.index((category, qnt)) < 5
    ]
