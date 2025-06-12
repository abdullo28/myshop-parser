from flask import Flask, request
from parser import search_texnomart

app = Flask(__name__)

@app.route("/parse-prices")
def parse_prices():
    query = request.args.get("query", "").strip().lower()
    items = search_texnomart(query)

    if not items:
        return f"<b>Цены не найдены по запросу:</b> {query}"

    html = f"<b>Результаты по запросу:</b> {query}<ul>"
    for item in items:
        html += f"<li><b>{item['store']}</b>: {item['price']} — <a href='{item['link']}' target='_blank'>Купить</a></li>"
    html += "</ul>"

    return html