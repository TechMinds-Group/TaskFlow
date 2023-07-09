"""Serializers do namespace espaco_de_trabalho"""
from uuid import uuid4
from flask_restx import fields
from server.api import api

trabalho_serializer = api.model(
    'EspacoDeTrabalho',
    {
        'id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do espaço de trabalho'
        ),
        'nome': fields.String(
            required=True,
            exemple='Nome do espaço de trabalho',
            description='Nome do espaço de trabalho'
        )

    }
)
