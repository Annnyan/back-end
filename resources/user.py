from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import USERS
from schemas import UserSchema

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user")
class UsersList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return USERS

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_data):
        if request_data["id"] in [u["id"] for u in USERS]:
            abort(400, message="ID must be unique")
        if request_data["name"] in [u["name"] for u in USERS]:
            abort(400, message="Name must be unique")
        USERS.append(request_data)
        return request_data
