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
