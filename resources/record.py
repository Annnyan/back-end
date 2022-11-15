from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import RECORDS, USERS, CATEGORIES
from schemas import RecordSchema, RecordQuerySchema

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("user_id")
        category_id = kwargs.get("category_id")
        records = []
        if not user_id:
            abort(400, message="Need at least user_id")
        if category_id:
            for record in RECORDS:
                if (
                        record["category_id"] == int(category_id)
                        and record["user_id"] == int(user_id)
                ):
                    records.append(record)
            return records
        for record in RECORDS:
            if record["user_id"] == int(user_id):
                records.append(record)
        return records


    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_data):
        if request_data["id"] in [u["id"] for u in RECORDS]:
            abort(400, message="ID must be unique")
        if request_data["user_id"] not in [u["id"] for u in USERS]:
            abort(400, message="User not found")
        if request_data["category_id"] not in [u["id"] for u in CATEGORIES]:
            abort(400, message="Category not found")
        RECORDS.append(request_data)
        return request_data
