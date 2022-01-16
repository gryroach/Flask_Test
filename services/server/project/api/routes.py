from flask import current_app as app, request, jsonify

from .models import Documents, Rights
from datetime import datetime
from .. import db
from .schemas import DocumentsSchema, RightsSchema

from marshmallow import ValidationError
from sqlalchemy import engine, func
from sqlalchemy.orm import scoped_session, sessionmaker

document_schema = DocumentsSchema()
right_schema = RightsSchema()


@app.route('/document', methods=['GET'])
def documents():
    response = [document.to_json() for document in Documents.query.all()]
    return jsonify(response)


@app.route('/document/add', methods=['POST'])
def document_add():
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
def document_update(id):
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
    return jsonify({'message': f'Document {status}!'})


@app.route('/document/<id>/delete', methods=['DELETE'])
def document_delete(id):
    inst = Documents.query.get_or_404(id)
    db.session.delete(inst)
    db.session.commit()
    return jsonify({'message': f'Document {id} deleted!'})


@app.route('/document/<id>', methods=['GET'])
def document_get(id):
    inst = Documents.query.get_or_404(id)
    return jsonify(inst.to_json())


@app.route('/rights/add', methods=['POST'])
def right_add():
    post_data = request.get_json()
    inserted_at = str(datetime.now())
    updated_at = str(datetime.now())
    data = {'name': post_data.get('name'), 'text': post_data.get('text'),
            'rights_from': post_data.get('rights_from'), 'rights_to': post_data.get('rights_to'),
            'inserted_at': inserted_at, 'updated_at': updated_at, 'document_id': post_data.get('document_id')}
    sess = scoped_session(sessionmaker(bind=engine))
    try:
        right = right_schema.load(data, session=sess)
    except ValidationError:
        return jsonify({'message': 'data is not valid!'})

    ex_docs = [str(item.id) for item in Documents.query.all()]
    if post_data.get('document_id') not in ex_docs:
        return jsonify({'message': 'document is not exist!'})

    db.session.add(right)
    db.session.commit()
    return jsonify({'message': 'Right added!'})


@app.route('/rights', methods=['GET'])
def rights():
    response = [right.to_json() for right in Rights.query.all()]
    return jsonify(response)


@app.route('/rights/<id>/update', methods=['PUT'])
def right_update(id):
    put_data = request.get_json()
    inserted_at = str(datetime.now())
    updated_at = str(datetime.now())
    data = {'name': put_data.get('name'), 'text': put_data.get('text'),
            'rights_from': put_data.get('rights_from'), 'rights_to': put_data.get('rights_to'),
            'inserted_at': inserted_at, 'updated_at': updated_at, 'document_id': put_data.get('document_id')}
    sess = scoped_session(sessionmaker(bind=engine))
    try:
        right = right_schema.load(data, session=sess)
    except ValidationError:
        return jsonify({'message': 'data is not valid!'})

    ex_docs = [str(item.id) for item in Documents.query.all()]
    if put_data.get('document_id') not in ex_docs:
        return jsonify({'message': 'document is not exist!'})

    inst = Rights.query.get(id)
    if inst:
        inst.name = right.name
        inst.text = right.text
        inst.rights_from = right.rights_from
        inst.rights_to = right.rights_to
        inst.updated_at = updated_at
        status = 'updated'
    else:
        db.session.add(right)
        status = 'created'
    db.session.commit()
    return jsonify({'message': f'Right {status}!'})


@app.route('/rights/<id>/delete', methods=['DELETE'])
def right_delete(id):
    inst = Rights.query.get_or_404(id)
    db.session.delete(inst)
    db.session.commit()
    return jsonify({'message': f'Right {id} deleted!'})


@app.route('/rights/<id>', methods=['GET'])
def right_get(id):
    inst = Rights.query.get_or_404(id)
    return jsonify(inst.to_json())
