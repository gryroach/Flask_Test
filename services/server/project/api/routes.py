from flask import current_app as app


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }
