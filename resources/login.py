from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import Blueprint, abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from models import UserModel
from schemas import UserSchema

blp = Blueprint("login", __name__, description="Operations on user")


@blp.route("/login")
class UsersList(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter_by(username=user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return jsonify({"access_token": access_token})
        else:
            abort(400, message="Incorrect password or username")
