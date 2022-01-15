from flask import current_app as app, request, jsonify
from .models import Documents, Rights


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }


@app.route('/documents/', methods=['GET', 'POST'])
def documents_list():
    documents = [document.to_json() for document in Documents.query.all()]
    return jsonify(documents)
