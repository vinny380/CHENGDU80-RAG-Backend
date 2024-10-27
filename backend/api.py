# app.py
from flask import Flask, jsonify, request


from agents import embed
from backend.src import RAG
app = Flask(__name__)

@app.route("/index", methods=["POST"])
def index():
    data = request.get_json()
    #for testing
    docs = RAG.index_documents()
    results = RAG.index_documents(docs)
    if results:
        return jsonify({"len of index items:": str(len(results))}), 200
    else:
        return jsonify({"nothing was indexed"}), 400

@app.route("/search", methods=["GET"])
def search():
    # Get the search term from query parameters
    search_term = request.args.get("term")
    search_term = embed.embed(search_term)
    results = RAG.search_with_vector(search_term)
    
    if search_term:
        return jsonify({"results": results})
    else:
        return jsonify({"error": "No search term provided"}), 400
    

if __name__ == "__main__":
    app.run(debug=True)