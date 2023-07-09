"""Forms para o namespace espacos."""
from flask_restx.reqparse import RequestParser


criar_espaco_parser = RequestParser()
form = criar_espaco_parser
form.add_argument(
    'nome',
    type=str,
    required=True,
    location='json'
)
form.add_argument(
    'espaco_de_trabalho_id',
    type=str,
    required=True,
    location='json'
)
