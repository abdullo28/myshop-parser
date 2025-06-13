from flask import Flask, request, jsonify
from parser import search_products

app = Flask(__name__)

@app.route("/")
def home():
    return "Kattabozor Parser API is running."

@app.route("/parse")
def parse():
    query = request.args.get("query", "").strip()
    if not query:
        return jsonify({"error": "Query is empty"}), 400

    try:
        results = search_products(query)
        if not results:
            return jsonify({"message": "No results found."}), 404
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
