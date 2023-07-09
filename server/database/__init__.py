"""Módulo de inicialização do banco de dados"""
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    """Inicializa as extensões"""
    db.init_app(app)
    import_module('server.database.models')
    return db
