"""Módulo de inicialização da API"""
from importlib import import_module
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restx import Api
from flask import Flask


api = Api()


@api.errorhandler
def handle_error(error):
    """Tratamento de erros da api"""
    if isinstance(error, NoAuthorizationError):
        return {'message': 'Token não encontrado'}, 401
    return {'message': 'Erro interno do servidor'}, 500


def init_app(app: Flask):
    """Iniciando a api"""
    app.config['ERROR_404_HELP'] = False
    api.init_app(app)
    import_module('server.api.namespaces')
    return api
