from flask import Flask, request, jsonify
from parser import search_products

app = Flask(__name__)

@app.route("/parse")
def parse():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "Query is empty"}), 400
    results = search_products(query)
    return jsonify(results)
