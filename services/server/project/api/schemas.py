from .models import Documents, Rights

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields


class DocumentsSchema(SQLAlchemySchema):
    class Meta:
        model = Documents
        load_instance = True

    id = auto_field()
    name = auto_field()
    text = auto_field()
    inserted_at = auto_field()
    updated_at = auto_field()
    right = auto_field()


class RightsSchema(SQLAlchemySchema):
    class Meta:
        model = Rights
        load_instance = True

    id = auto_field()
    name = auto_field()
    text = auto_field()
    rights_from = auto_field()
    rights_to = auto_field()
    inserted_at = auto_field()
    updated_at = auto_field()
    document_id = auto_field()
