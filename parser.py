from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def search_products(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = f"https://www.kattabozor.uz/search?query={query}"
        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)
        html = page.content()
        browser.close()

        soup = BeautifulSoup(html, "html.parser")
        items = []
        for item in soup.select("a.product-card__container"):
            title = item.select_one(".product-card__title")
            price = item.select_one(".product-card__price")
            link = "https://www.kattabozor.uz" + item.get("href", "")
            if title and price:
                items.append({
                    "title": title.text.strip(),
                    "price": price.text.strip(),
                    "link": link
                })
        return items
