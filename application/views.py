from flask import jsonify, request
from application import app
from application.db import USERS, CATEGORIES, RECORDS

@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/records")
def get_records():
    return jsonify({"records": RECORDS})


@app.route("/userrecords")
def get_user_records():
    user_id = request.args.get("userid")
    category_id = request.args.get("categoryid")
    records = []
    if category_id:
        for record in RECORDS:
            if record["category_id"] == int(category_id) and record["user_id"] == int(user_id):
                records.append(record)
        return jsonify({"records": records})
    for record in RECORDS:
        if record["user_id"] == int(user_id):
            records.append(record)
    return jsonify({"records": records})


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


@app.route("/addrecord", methods=["POST"])
def add_record():
    request_data = request.get_json()
    for record in RECORDS:
        if record["id"] == request_data["id"]:
            return "Please, enter another id"
    RECORDS.append(request_data)
    return request_data
