from flask import current_app
# from sqlalchemy.sql import func

from project import db


class Documents(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(255), nullable=True)
    inserted_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    right = db.relationship('Rights', backref='document', lazy=True, cascade='all,delete')

    def __init__(self, name, text, inserted_at, updated_at):
        self.name = name
        self.text = text
        self.inserted_at = inserted_at
        self.updated_at = updated_at

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'inserted_at': self.inserted_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return f"<documents {self.id}>"


class Rights(db.Model):
    __tablename__ = 'rights'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(255), nullable=True)
    rights_from = db.Column(db.DateTime, nullable=True)
    rights_to = db.Column(db.DateTime, nullable=True)
    inserted_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)

    def __init__(self, name, text, document_id, rights_from, rights_to, inserted_at, updated_at):
        self.name = name
        self.text = text
        self.rights_from = rights_from
        self.rights_to = rights_to
        self.inserted_at = inserted_at
        self.updated_at = updated_at
        self.document_id = document_id

    def __str__(self):
        return f"<rights {self.id}>"
