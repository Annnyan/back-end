from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import RecordModel, CategoryModel
from schemas import RecordSchema, RecordQuerySchema
from sqlalchemy.exc import IntegrityError

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        if category_id:
            query = RecordModel.query.filter_by(user_id=user_id, category_id=category_id)
            return query
        query = RecordModel.query.filter_by(user_id=user_id)
        return query

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        note = RecordModel(**record_data)
        category_id = record_data.get("category_id")
        categories = CategoryModel.query.with_entities(CategoryModel.owner_id)
        owner_id = categories.filter_by(id=category_id).scalar()
        if owner_id == record_data["user_id"] or owner_id is None:
            try:
                db.session.add(note)
                db.session.commit()
            except IntegrityError:
                abort(400, message="Error when creating note")
            return note
        else:
            abort(403, message="Access is denied")
