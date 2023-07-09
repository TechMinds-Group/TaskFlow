"""Módulo de inicialização do banco de dados"""
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from loguru import logger

db = SQLAlchemy()


def init_app(app: Flask):
    """Inicializa o banco de dados."""
    logger.info('🔧 Inicializando o banco de dados.')
    db.init_app(app)
    import_module('server.database.models')
    return db
