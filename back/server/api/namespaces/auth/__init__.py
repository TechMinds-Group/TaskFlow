"""Rotas relacionadas a autenticação"""
from flask_restx import Resource, abort
from loguru import logger
from server.database.models import Usuario
from server.api import api
from .forms import login_parser
from .serializers import auth_serializer


np_auth = api.namespace(
    'auth',
    description='Operações relacionadas a autenticação'
)


class AuthResource(Resource):
    """Classe de recursos de autenticação"""

    @np_auth.expect(login_parser, validate=True)
    @np_auth.marshal_with(auth_serializer, code=200)
    def post(self):
        """Retorna um token de autenticação"""
        payload = login_parser.parse_args()
        username = payload['username']
        user = Usuario.query.filter(
            Usuario.username == username
        ).first()
        if not user or not user.check_password(payload['password']):
            logger.debug(
                f'🤖 Usuario {username} tentou acessar o sistema.'
            )
            abort(401, message='Credenciais inválidas')
        logger.debug(f'🤖 Usuario {username} fez login no sistema.')
        return {'token': user.generate_token()}, 200


np_auth.add_resource(AuthResource, '/', endpoint='auth')
