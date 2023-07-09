"""Módulo de inicialização da API"""
from importlib import import_module
from flask_restx import Api
from flask import Flask


api = Api()


def init_app(app: Flask):
    """Iniciando a api"""
    app.config['ERROR_404_HELP'] = False
    api.init_app(app)
    import_module('server.api.namespaces')
    return api
