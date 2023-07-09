"""Rotas de usuários"""
import re
from flask_restx import Resource, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError
from server.api import api
from server.database.models import Usuario
from .serializers import usuario_serializer
from .forms import criar_usuario_parser

np_usuarios = api.namespace(
    'usuarios', description='Operações relacionadas a usuários')


class UsuarioResource(Resource):
    """Classe de recursos de usuários"""

    def query_for_id(self, usuario_id):
        """Retorna um usuário pelo id ou levanta 404"""
        user = Usuario.query.filter(
            Usuario.id == str(usuario_id)
        ).first()
        if not user:
            abort(404, message='Usuário não encontrado')
        return user

    @np_usuarios.marshal_with(usuario_serializer)
    @jwt_required()
    def get(self, usuario_id=None):
        """Retorna um usuário pelo id ou todos os usuários"""
        if usuario_id:
            users = self.query_for_id(usuario_id)
        else:
            users = Usuario.query.all()

        return users, 200

    @np_usuarios.expect(criar_usuario_parser, validate=True)
    @np_usuarios.marshal_with(usuario_serializer, code=201)
    def post(self):
        """Cria um novo usuário"""
        payload = criar_usuario_parser.parse_args()
        user = Usuario()
        user.insert_credentials(**payload)
        user.insert_perfil(**payload)
        try:
            user.add()
        except IntegrityError as error:
            user.rollback()
            message = re.search(r'UNIQUE[\w\W]+usuario.(\w+)', str(error))
            if message:
                abort(
                    409,
                    message='Entrada Invalida',
                    errors={message.group(1): 'username já em uso'}
                )
            abort(500, message='Erro interno do servidor')
        user.save()
        return user, 201


np_usuarios.add_resource(
    UsuarioResource,
    '/',
    methods=['GET', 'POST']
)
np_usuarios.add_resource(
    UsuarioResource,
    '/<uuid:usuario_id>',
    methods=['GET']
)
