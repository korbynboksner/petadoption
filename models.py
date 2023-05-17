from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                     nullable=False)
    image_url = db.Column(db.Text)
    age = db.Column(db.Text,)
    notes = db.Column(db.Text,)
    available = db.Column(db.Boolean, nullable=False, default=True)




def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)