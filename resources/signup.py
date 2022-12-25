from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from db import db
from models import UserModel
from schemas import UserSchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("signup", __name__, description="Operations on user")


@blp.route("/signup")
class UsersList(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(
            username=user_data["username"], password=pbkdf2_sha256.hash(user_data["password"]),
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Name is taken")
        return user
