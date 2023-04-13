import requests
import time
from parsel import Selector


def fetch(url):
    try:
        resp = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
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
    selector = Selector(html_content)
    all_urls = selector.css(".entry-title a::attr(href)").getall()

    return all_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css("a.next::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    infos = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("li.meta-author span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text")
            .get()
            .split("minutos")[0]
        ),
        "summary": "".join(
            selector.css("div.entry-content > p:nth-of-type(1)::text").getall()
        ).strip(),
        "category": selector.css(".meta-category a span.label::text").get(),
    }

    return infos


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
