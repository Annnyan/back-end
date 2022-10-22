from flask import jsonify, request
from application import app

CATEGORIES = [
    {
        "id": 1,
        "name": "food"
    }
]

@app.route("/categories")
def get_categories():
    return jsonify({"categiries": CATEGORIES})

@app.route("/category", methods=["POST"])
def create_category():
    request_data = request.get_json()
    CATEGORIES.append(request_data)
    return request_data

