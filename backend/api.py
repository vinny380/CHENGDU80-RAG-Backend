# app.py
from flask import Flask, jsonify, request
import json

from agents import embed,completion
from backend.src import RAG,Dynamic_policy_speed,Dynamic_policy_aggressive
app = Flask(__name__)

@app.route("/complete", methods=["POST"])
def complete():
    prompt = request.get_json()["prompt"]
    response = completion.complete(prompt)
    response_json = json.loads(response.content)
    return jsonify(response_json), 200
    

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
    




@app.route("/speed", methods=["GET"])
def dynamicpolicy_speed():
    liabilities,premiums,speeds = Dynamic_policy_speed.speed_dynamic()
    
    if liabilities:
        return jsonify({"liabilities":liabilities,"premiums":premiums,"speeds":speeds.to_dict()}),200
    else:
        return jsonify({"error": "No results are provided"}), 400
    



@app.route("/aggressive", methods=["GET"])
def dynamicpolicy_aggressive():
    liabilities,premiums,ratios = Dynamic_policy_aggressive.agg_dynamic()
    if liabilities:
        return jsonify({"liabilities":liabilities,"premiums":premiums,"ratios":ratios}),200
    else:
        return jsonify({"error": "No results are provided"}), 400
    






if __name__ == "__main__":
    app.run(debug=True)