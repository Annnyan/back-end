from flask import jsonify, request
from application import app

CATEGORIES = [
    {
        "id": 1,
        "name": "food"
    }
]

USERS = [
    {
        "id": 1,
        "name": "Anna"
    }
]

NOTES = [
    {
        "id": 1,
        "user_id": 1,
        "category_id": 1,
        "date": "2022-10-22 11:40",
        "expenses": 350
    }
]


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/notes")
def get_notes():
    return jsonify({"notes": NOTES})


@app.route("/usernotes")
def get_user_notes():
    user_id = request.args.get("userid")
    category_id = request.args.get("categoryid")
    notes = []
    if category_id:
        for note in NOTES:
            if note["category_id"] == int(category_id) and note["user_id"] == int(user_id):
                notes.append(note)
        return jsonify({"notes": notes})
    for note in NOTES:
        if note["user_id"] == int(user_id):
            notes.append(note)
    return jsonify({"notes": notes})


@app.route("/adduser", methods=["POST"])
def add_user():
    request_data = request.get_json()
    for user in USERS:
        if user["id"] == request_data["id"]:
            return "Please, enter another id"
    USERS.append(request_data)
    return request_data


@app.route("/addcategory", methods=["POST"])
def add_category():
    request_data = request.get_json()
    for category in CATEGORIES:
        if category["id"] == request_data["id"]:
            return "Please, enter another id"
    CATEGORIES.append(request_data)
    return request_data


@app.route("/addnote", methods=["POST"])
def add_note():
    request_data = request.get_json()
    for note in NOTES:
        if note["id"] == request_data["id"]:
            return "Please, enter another id"
    NOTES.append(request_data)
    return request_data
