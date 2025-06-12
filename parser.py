import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def search_texnomart(query):
    url = f"https://texnomart.uz/ru/search?q={query.replace(' ', '%20')}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for item in soup.select(".products__item"):
        title = item.select_one(".products__item__info-title")
        price = item.select_one(".products__item-price-new")
        link = item.select_one("a")

        if title and price and link:
            results.append({
                "store": "Texnomart.uz",
                "price": price.text.strip(),
                "link": "https://texnomart.uz" + link["href"]
            })

    return results