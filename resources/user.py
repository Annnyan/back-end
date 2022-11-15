from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import UserModel
from schemas import UserSchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user")
class UsersList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Name is taken")
        return user
