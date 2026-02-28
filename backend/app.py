from flask import Flask, request, jsonify

try:
    from backend.graph import app as langgraph_app
except ImportError: 
    import sys, os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root not in sys.path:
        sys.path.insert(0, root)
    from backend.graph import app as langgraph_app

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "running"}


@app.route("/query", methods=["POST"])
def query():

    user_query = None
    if request.method == "POST":
    
        data = request.get_json(silent=True) or {}
        user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "query parameter is required"}), 400

    result = langgraph_app.invoke({
        "query": user_query
    })

    return jsonify({
        "response": result.get("response"),
        "status": result.get("status")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)