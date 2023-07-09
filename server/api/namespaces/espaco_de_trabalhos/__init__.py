"""Rotas relacionadas a espaço de trabalho"""
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, abort
from sqlalchemy.exc import IntegrityError
from server.api import api
from server.database.models import EspacoDeTrabalho, Membro
from .serializers import trabalho_serializer, membro_serializer
from .forms import criar_trabalho_parser


np_espaco_de_trabalhos = api.namespace(
    'espaco_de_trabalhos', description='Espaço de trabalho')


class EspacoDeTrabalhoResource(Resource):
    """Classe de recursos de espaço de trabalho"""

    @np_espaco_de_trabalhos.marshal_with(trabalho_serializer)
    @jwt_required()
    def get(self, espaco_de_trabalho_id=None):
        """Retorna um espaço de trabalho pelo id
        ou todos os espaços de trabalho"""
        if espaco_de_trabalho_id:
            trabalhos = EspacoDeTrabalho.query_with_user(
                usuario_id=get_jwt_identity(),
                espaco_de_trabalho_id=espaco_de_trabalho_id
            )
            if not trabalhos:
                abort(404, message='Espaço de trabalho não encontrado')
        else:
            trabalhos = EspacoDeTrabalho.query_with_user(
                usuario_id=get_jwt_identity()
            )
        return trabalhos, 200

    @np_espaco_de_trabalhos.marshal_with(trabalho_serializer)
    @np_espaco_de_trabalhos.expect(criar_trabalho_parser, validate=True)
    @jwt_required()
    def post(self):
        """Cria um novo espaço de trabalho"""
        payload = criar_trabalho_parser.parse_args()
        usuario_id = get_jwt_identity()

        trabalho = EspacoDeTrabalho()
        trabalho.insert_espaco_de_trabalho(**payload)

        try:
            trabalho.add()
        except IntegrityError:
            trabalho.rollback()
            abort(500, message='Erro ao criar espaço de trabalho')
        try:
            trabalho.add_membro(usuario_id)
        except IntegrityError:
            trabalho.rollback()
            abort(
                500,
                message='Erro ao adicionar membro ao espaço de trabalho'
            )
        trabalho.save()
        return trabalho, 201


class EspacoDeTrabalhoMembroResource(Resource):
    """Classe de recursos de membros de espaço de trabalho"""
    def get_with_espaco_de_trabalho_id(
            self, espaco_de_trabalho_id, membro_id=None):
        """Retorna um membro de um espaco_de_trabalho_id
        pelo id ou todos os membros"""
        query = Membro.query.filter(
            Membro.espaco_de_trabalho_id == str(espaco_de_trabalho_id)
        )
        if membro_id:
            return query.filter(Membro.id == str(membro_id)).first()
        return query.all()

    @np_espaco_de_trabalhos.marshal_with(membro_serializer)
    def get(self, espaco_de_trabalho_id=None, membro_id=None):
        """Retorna um membro pelo id ou todos os membros"""
        if espaco_de_trabalho_id:
            membros = self.get_with_espaco_de_trabalho_id(
                espaco_de_trabalho_id, membro_id
            )
        else:
            membros = Membro.query.filter(
                Membro.id == str(membro_id)
            ).first()

        if not membros:
            abort(404, message='Membro não encontrado')

        return membros, 200


np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoResource,
    '/',
    methods=['POST', 'GET']
)
np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoResource,
    '/<uuid:espaco_de_trabalho_id>/',
    methods=['GET']
)
np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoMembroResource,
    '/<uuid:espaco_de_trabalho_id>/membros/',
    methods=['GET']
)
np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoMembroResource,
    '/<uuid:espaco_de_trabalho_id>/membros/<uuid:membro_id>/',
    methods=['GET']
)
np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoMembroResource,
    '/membros/<uuid:membro_id>/',
    methods=['GET']
)
