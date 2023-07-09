"""Módulo de formulários da usuários"""
from flask_restx.reqparse import RequestParser


criar_usuario_parser = RequestParser()
form = criar_usuario_parser
form.add_argument(
    'username',
    type=str,
    required=True,
    trim=True,
    location='json',
)
form.add_argument(
    'password',
    type=str,
    required=True,
    location='json',
)
form.add_argument(
    'nome',
    type=str,
    required=True,
    location='json',
)
