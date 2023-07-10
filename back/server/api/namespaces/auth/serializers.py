"""Serializadores para o namespace de autenticação"""""
from flask_restx import fields
from server.api import api

auth_serializer = api.model(
    'Auth',
    {
        'token': fields.String(
            required=True,
            description='Token de autenticação'
        )
    }
)
