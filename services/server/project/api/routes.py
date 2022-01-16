import datetime

from flask import current_app as app, request, jsonify


from .models import Documents, Rights
from datetime import datetime
from .. import db
from .schemas import DocumentsSchema, RightsSchema

from marshmallow import ValidationError
from sqlalchemy import engine
from sqlalchemy.orm import scoped_session, sessionmaker

document_schema = DocumentsSchema()
right_schema = RightsSchema()


@app.route('/document/', methods=['GET', 'POST'])
def documents():
    response = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        text = post_data.get('text')
        inserted_at = datetime.now()
        updated_at = datetime.now()
        db.session.add(Documents(name=name, text=text, inserted_at=inserted_at, updated_at=updated_at))
        db.session.commit()
        response['message'] = 'Document added!'
    else:
        response['documents'] = [document.to_json() for document in Documents.query.all()]
    return jsonify(response)


@app.route('/document/add', methods=['POST'])
def documents_add():
    post_data = request.get_json()
    name = post_data.get('name')
    text = post_data.get('text')
    inserted_at = str(datetime.now())
    updated_at = str(datetime.now())
    data = {'name': name, 'text': text, 'inserted_at': inserted_at, 'updated_at': updated_at}
    sess = scoped_session(sessionmaker(bind=engine))
    try:
        document = document_schema.load(data, session=sess)
    except ValidationError:
        return jsonify({'message': 'data is not valid!'})
    db.session.add(document)
    db.session.commit()
    return jsonify({'message': 'Document added!'})


@app.route('/document/<id>/update', methods=['PUT', 'PATCH'])
def documents_update(id):
    post_data = request.get_json()
    name = post_data.get('name')
    text = post_data.get('text')
    inserted_at = datetime.now()
    updated_at = datetime.now()
    db.session.add(Documents(name=name, text=text, inserted_at=inserted_at, updated_at=updated_at))
    db.session.commit()
    return jsonify({'message': 'Document added!'})