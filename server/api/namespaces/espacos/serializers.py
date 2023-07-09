"""Serializers para o namespace de espacos."""
from uuid import uuid4
from flask_restx import fields
from server.api import api


espaco_serializer = api.model(
    'Espaco',
    {
        'id': fields.String(
            example=str(uuid4()),
            required=True,
        ),
        'nome': fields.String(
            example='Espaço de trabalho',
            required=True,
        ),
        'espaco_de_trabalho_id': fields.String(
            example=str(uuid4()),
            required=True,
        )
    }
)

membro_espaco_serializer = api.model(
    'Membro',
    {
        'id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do membro'
        ),
        'espaco_id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do Espaco'
        ),
        'membro_id': fields.String(
            required=True,
            example=str(uuid4()),
            description='Id do Membro'
        ),
    }
)
