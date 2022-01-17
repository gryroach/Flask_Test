import pytest
import os
from manage import app

# from project import create_app, db


client = app.test_client()


# @pytest.fixture
# def app():
#     app = create_app()
#     app_settings = os.getenv('APP_SETTINGS')
#     app.config.from_object(app_settings)
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.drop_all()
#         db.create_all()


def test_post_document():
    document = {'name': 'doc_client', 'text': 'test_text'}
    res = client.post('/document/add', json=document)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document added!'

    incor_document = {'incor_name': 'doc1', 'text': 'test_text'}
    res = client.post('/document/add', json=incor_document)
    assert res.status_code == 400

    res = client.put('/document/add', json=document)
    assert res.status_code == 405


def test_put_document():
    document = {'name': 'doc1', 'text': 'test_text'}
    res = client.put('/document/1/update', json=document)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document updated!'

    res = client.put('/document/2/update', json=document)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document created!'

    incor_document = {'incor_name': 'doc1', 'text': 'test_text'}
    res = client.put('/document/1/update', json=incor_document)
    assert res.status_code == 400

    res = client.post('/document/1/update', json=document)
    assert res.status_code == 405


def test_get_all_documents():
    res = client.get('/document')
    assert res.status_code == 200
    assert type(res.get_json()) == list

    res = client.post('/document')
    assert res.status_code == 405


def test_get_one_document():
    res = client.get('/document/1')
    assert type(res.get_json()) == dict
    assert res.status_code == 200


def test_delete_document():
    res = client.delete('/document/2/delete')
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document 2 deleted!'


def test_post_right():
    right = {'name': 'right1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
             'rights_to': '2022-01-17 18:37:55', 'document_id': '1'}
    res = client.post('/rights/add', json=right)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Right added!'

    bad_right = {'name': 'right1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
                 'rights_to': '2022-01-17 18:37:55', 'document_id': '10'}
    res = client.post('/rights/add', json=bad_right)
    assert res.status_code == 400

    incor_right = {'incor_name': 'doc1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
                   'rights_to': '2022-01-17 18:37:55', 'document_id': '1'}
    res = client.post('/rights/add', json=incor_right)
    assert res.status_code == 400

    res = client.put('/rights/add', json=right)
    assert res.status_code == 405


def test_put_right():
    right = {'name': 'right1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
             'rights_to': '2022-01-17 18:37:55', 'document_id': '1'}
    res = client.put('/rights/1/update', json=right)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Right updated!'

    res = client.put('/rights/2/update', json=right)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Right created!'

    bad_right = {'name': 'right1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
                 'rights_to': '2022-01-17 18:37:55', 'document_id': '10'}
    res = client.put('/rights/add', json=bad_right)
    assert res.status_code == 405

    incor_right = {'incor_name': 'right1', 'text': 'test_text', 'rights_from': '2022-01-17 18:37:55',
                   'rights_to': '2022-01-17 18:37:55', 'document_id': '1'}
    res = client.put('/rights/1/update', json=incor_right)
    assert res.status_code == 400

    res = client.post('/rights/1/update', json=right)
    assert res.status_code == 405


def test_get_all_rights():
    res = client.get('/rights')
    assert res.status_code == 200
    assert type(res.get_json()) == list

    res = client.post('/rights')
    assert res.status_code == 405


def test_get_one_right():
    res = client.get('/rights/1')
    assert type(res.get_json()) == dict
    assert res.status_code == 200


def test_delete_right():
    res = client.delete('/rights/2/delete')
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Right 2 deleted!'
