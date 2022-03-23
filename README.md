# Flask application with database
Flask app for working with Postgres database with CRUD endpoints for two models: Documents and Rights

## Launch of the project

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/gryroach/Flask_Test.git
$ cd Flask_Test
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```
Install the dependencies for django project:
```sh
(env)$ pip install -r .services/server/requirements.txt
```
Create .env file to configure database settings:
```sh
(env)$ touch .env
(env)$ nano .env
```
Set the following environment variables:
- POSTGRES_USER
- POSTGRES_PASSWORD

Run containers:
```sh
(env)$ docker-compose up --build -d
```
## Work
### links
- GET -> http://127.0.0.1:5000/document - get all documents
- GET -> http://127.0.0.1:5000/document/{id} - get document with id
- POST -> http://127.0.0.1:5000/document/add - add new document
- PUT -> http://127.0.0.1:5000/document/{id}/update - update document with id
- DELETE -> http://127.0.0.1:5000/document/{id}/delete - delete document with id
- GET -> http://127.0.0.1:5000/rights - get all rights
- GET -> http://127.0.0.1:5000/rights/{id} - get right with id
- POST -> http://127.0.0.1:5000/rights/add - add new right
- PUT -> http://127.0.0.1:5000/rights/{id}/update - update right with id
- DELETE -> http://127.0.0.1:5000/rights/{id}/delete - delete right with id

### example of data
- document:
```json
{
    "name": "document_new",
    "text": "test_text"
}
```
- right:
```json
{
    "name": "right_new",
    "text": "test__right_text",
    "rights_from": "2022-01-17 18:37:55",
    "rights_to": "2022-01-18 18:37:55",
    "document_id": "1"
}
```
> **NOTE**: **id, inserted_at and updated_at fields are created automatically**
