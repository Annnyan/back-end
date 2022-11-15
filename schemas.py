from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    date = fields.Str(required=True)
    sum = fields.Float(required=True)

class RecordQuerySchema(Schema):
    user_id = fields.Int()
    category_id = fields.Int()
