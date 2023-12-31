"""Módulo de serializadores de usuários"""
from uuid import uuid4
from flask_restx import fields
from server.api import api
from ..espaco_de_trabalhos.serializers import membro_serializer

usuario_serializer = api.model('Usuario', {
    'id': fields.String(
        required=True,
        description='ID do usuário',
        example=str(uuid4())
    ),
    'username': fields.String(
        required=True,
        description='Nome de usuário',
        example='joao.silva'
    ),
    'nome': fields.String(
        required=True,
        description='Nome do usuário',
        example='João da Silva'
    ),
    'membros': fields.List(
        fields.Nested(membro_serializer)
    )
})
