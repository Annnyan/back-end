from flask.views import MethodView
from flask_smorest import Blueprint, abort

from application.db import CATEGORIES
from application.schemas import CategorySchema

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CATEGORIES

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_data):
        if request_data["id"] in [u["id"] for u in CATEGORIES]:
            abort(400, message="ID must be unique")
        if request_data["name"] in [u["name"] for u in CATEGORIES]:
            abort(400, message="Name must be unique")
        CATEGORIES.append(request_data)
        return request_data
