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
    inserted_at = str(datetime.now())
    updated_at = str(datetime.now())
    data = {'name': post_data.get('name'), 'text': post_data.get('text'),
            'inserted_at': inserted_at, 'updated_at': updated_at}
    sess = scoped_session(sessionmaker(bind=engine))
    try:
        document = document_schema.load(data, session=sess)
    except ValidationError:
        return jsonify({'message': 'data is not valid!'})
    db.session.add(document)
    db.session.commit()
    return jsonify({'message': 'Document added!'})


@app.route('/document/<id>/update', methods=['PUT'])
def documents_update(id):
    put_data = request.get_json()
    inserted_at = str(datetime.now())
    updated_at = str(datetime.now())
    data = {'name': put_data.get('name'), 'text': put_data.get('text'),
            'inserted_at': inserted_at, 'updated_at': updated_at}
    sess = scoped_session(sessionmaker(bind=engine))
    try:
        document = document_schema.load(data, session=sess)
    except ValidationError:
        return jsonify({'message': 'data is not valid!'})
    inst = Documents.query.get(id)
    if inst:
        inst.name = document.name
        inst.text = document.text
        inst.updated_at = updated_at
        status = 'updated'
    else:
        db.session.add(document)
        status = 'created'
    db.session.commit()
    return jsonify({'message': f'Document {id} {status}!'})


@app.route('/document/<id>/delete', methods=['DELETE'])
def documents_delete(id):
    inst = Documents.query.get_or_404(id)
    db.session.delete(inst)
    db.session.commit()
    return jsonify({'message': f'Document {id} deleted!'})


@app.route('/document/<id>', methods=['GET'])
def document_get(id):
    inst = Documents.query.get_or_404(id)
    return jsonify(inst.to_json())
