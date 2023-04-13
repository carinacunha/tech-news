import requests
import time


def fetch(url):
    try:
        resp = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        if resp.status_code == 200:
            return resp.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
