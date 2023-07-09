"""Forms para o namespace espaco_de_trabalho."""""
from flask_restx.reqparse import RequestParser


criar_trabalho_parser = RequestParser()
form = criar_trabalho_parser
form.add_argument(
    'nome',
    required=True,
    description='Nome do espaço de trabalho',
    location='json',
)
