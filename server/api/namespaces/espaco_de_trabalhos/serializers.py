"""Serializers do namespace espaco_de_trabalho"""
from uuid import uuid4
from flask_restx import fields
from server.api import api
from ..espacos.serializers import membro_espaco_serializer

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
membro_serializer = api.model(
    'Membro',
    {
        'id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do membro'
        ),
        'usuario_id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do Usuario'
        ),
        'espaco_de_trabalho_id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do Espaço de trabalho'
        ),
        'espaco_de_trabalhos': fields.List(
            fields.Nested(trabalho_serializer)
        ),
        'membro_espacos': fields.List(
            fields.Nested(membro_espaco_serializer)
        )
    }
)
