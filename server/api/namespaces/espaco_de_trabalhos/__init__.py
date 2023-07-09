"""Rotas relacionadas a espaço de trabalho"""
# from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, abort
from flask_jwt_extended import jwt_required
from server.api import api
from .serializers import trabalho_serializer
from .forms import criar_trabalho_parser


np_espaco_de_trabalhos = api.namespace(
    'espaco_de_trabalhos', description='Espaço de trabalho')


class EspacoDeTrabalhoResource(Resource):
    """Classe de recursos de espaço de trabalho"""

    def query_for_id(self, trabalho_id):
        """Pega um espaço de trabalho pelo id ou levanta 404"""
        print(trabalho_id)
        # pylint: disable=W0105
        """
        trabalho = EspacoDeTrabalho.query.filter(
            EspacoDeTrabalho.id == trabalho_id
        ).first()
        if not trabalho:
        """
        abort(404, message='Espaço de trabalho não encontrado')
        # pylint: disable=W0105
        """
        return trabalho
        """

    @np_espaco_de_trabalhos.marshal_with(trabalho_serializer)
    @jwt_required()
    def get(self, trabalho_id=None):
        """Retorna um espaço de trabalho pelo id
        ou todos os espaços de trabalho"""
        if trabalho_id:
            trabalhos = self.query_for_id(trabalho_id)  # pylint: disable=E1111
        else:
            trabalhos = []
            # pylint: disable=W0105
            """
            trabalhos = EspacoDeTrabalho.query.all()
            """
        return trabalhos, 200

    @np_espaco_de_trabalhos.marshal_with(trabalho_serializer)
    @np_espaco_de_trabalhos.expect(criar_trabalho_parser, validate=True)
    @jwt_required()
    def post(self):
        """Cria um novo espaço de trabalho"""
        # pylint: disable=W0105
        """
        payload = criar_trabalho_parser.parse_args()
        usuario_id = get_jwt_identity()

        trabalho = EspacoDeTrabalho()
        trabalho.insert_infos(**payload)
        trabalho.create_membro(usuario_id)
        try:
            trabalho.add()
        except IntegrityError as error:
            trabalho.rollback()
            abort(500, message='Erro interno do servidor')
        trabalho.save()
        return trabalho, 201
        """
        print('post')


np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoResource,
    '/', methods=['POST', 'GET']
)
np_espaco_de_trabalhos.add_resource(
    EspacoDeTrabalhoResource,
    '/<uuid:trabalho_id>', methods=['GET']
)
