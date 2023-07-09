"""Módulo de inicialização da API"""
from importlib import import_module
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError
from flask_restx import Api
from flask import Flask
from loguru import logger


api = Api()


@api.errorhandler
def handle_error(error):
    """Tratamento de erros da api"""
    message = 'Erro interno do servidor'
    code = 500
    if isinstance(error, NoAuthorizationError):
        message = 'Token não encontrado'
        code = 401
    elif isinstance(error, ExpiredSignatureError):
        message = 'Token expirado'
        code = 401
    logger.critical(error)
    return {'message': message}, code


def init_app(app: Flask):
    """Iniciando a api"""
    logger.info('🔧 Inicializando a api.')
    app.config['ERROR_404_HELP'] = False
    api.init_app(app)
    import_module('server.api.namespaces')
    return api
