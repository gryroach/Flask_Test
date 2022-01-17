from manage import app

client = app.test_client()


def test_get_all_documents():
    res = client.get('/document')
    assert res.status_code == 200
    assert type(res.get_json()) == list

    res = client.post('/document')
    assert res.status_code == 405


def test_post_document():
    document = {'name': 'doc1', 'text': 'test_text'}
    res = client.post('/document/add', json=document)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document added!'

    document = {'incor_name': 'doc1', 'text': 'test_text'}
    res = client.post('/document/add', json=document)
    assert res.status_code == 400

    res = client.put('/document/add', json=document)
    assert res.status_code == 405


def test_get_one_documents():
    res = client.get('/document/1')
    assert res.status_code == 404


def test_put_document():
    document = {'name': 'doc1', 'text': 'test_text'}
    res = client.put('/document/1/update', json=document)
    assert res.status_code == 200
    assert res.get_json()['message'] == 'Document created!'

    document = {'incor_name': 'doc1', 'text': 'test_text'}
    res = client.put('/document/1/update', json=document)
    assert res.status_code == 400

    res = client.post('/document/1/update', json=document)
    assert res.status_code == 405


def test_delete_documents():
    res = client.delete('/document/1/delete')
    assert res.status_code == 404


