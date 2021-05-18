
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

import app
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = True)
    species = db.Column(db.String(50), nullable = True)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String(100))
    available = db.Column(db.Boolean, default = True)

