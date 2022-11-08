import requests

# Requisito 1
def fetch(url: str, wait: int = 1) -> str:
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=wait)
        response.raise_for_status()
    except (requests.ReadTimeout):
        return None
    else:
         return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
