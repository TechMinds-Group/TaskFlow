from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from importlib import import_module

db = SQLAlchemy()


def init_app(app: Flask):
    """Inicializa as extensões"""
    db.init_app(app)
    import_module('server.database.models')
    return db
