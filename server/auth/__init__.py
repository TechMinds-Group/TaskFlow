"""Módulo de autenticação"""
from flask_jwt_extended import JWTManager
from flask import Flask

jwt_manager = JWTManager()


def init_app(app: Flask):
    """Inicializa o JWT"""
    jwt_manager.init_app(app)
    return jwt_manager
