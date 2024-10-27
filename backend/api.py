# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Flask!"})

@app.route("/items/<int:item_id>")
def get_item(item_id):
    query_param = request.args.get("q")
    return jsonify({"item_id": item_id, "q": query_param})

if __name__ == "__main__":
    app.run(debug=True)
