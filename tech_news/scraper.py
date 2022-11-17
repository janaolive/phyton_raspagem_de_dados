import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=wait
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    news_url = selector.css(".entry-title a::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    news_url_next_page = selector.css("a.next::attr(href)").get()
    if news_url_next_page:
        return news_url_next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(
        "div.entry-header-inner h1.entry-title::text").getall()
    title = "".join(title).strip()
    timestamp = selector.css(
        "ul.post-meta li.meta-date::text").get()
    writer = selector.css(
        "ul.post-meta li.meta-author span.author a::text").get()
    comments_count = selector.css(
        "div.post-comments h5.title-block::text").re_first(r"\d")
    summary = selector.css(
        "div.entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary).strip()
    tags = selector.css(
        "section.post-tags li a[rel=tag]::text").getall()
    category = selector.css(
        "div.meta-category a span.label::text").get()
    news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count or 0,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    content_news = fetch("https://blog.betrybe.com/")
    links = scrape_novidades(content_news)
    while len(links) < amount:
        next_page = scrape_next_page_link(content_news)
        content_news = fetch(next_page)
        news_links = scrape_novidades(content_news)
        for new_link in news_links:
            links.append(new_link)
    news_data = []
    for index in range(amount):
        news_request = fetch(links[index])
        news_data.append(scrape_noticia(news_request))
    create_news(news_data)
    return news_data
