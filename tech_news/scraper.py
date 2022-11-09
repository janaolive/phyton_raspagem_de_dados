import requests
import time
from parsel import Selector


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


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
