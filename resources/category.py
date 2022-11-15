from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import CategoryModel
from schemas import CategorySchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, category_data):
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Name is taken")
        return category
