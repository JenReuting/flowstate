""" SQLAlchemy models for FlowState """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ Connect to database. """
    db.app = app
    db.init_app(app)
