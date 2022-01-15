import datetime

from flask import current_app as app, request, jsonify
from .models import Documents, Rights
from datetime import datetime
from .. import db


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }


@app.route('/documents/', methods=['GET', 'POST'])
def documents():
    response = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
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
