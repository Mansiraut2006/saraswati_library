from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    member_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='member')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Available')
    holder = db.Column(db.String(100), default='')
    requested_by = db.Column(db.String(100), default='')
    issue_date = db.Column(db.String(20), default='')
    due_date = db.Column(db.String(20), default='')