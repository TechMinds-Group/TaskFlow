"""Rotas para o namespace de espaços de trabalho"""
from flask_restx import Resource, abort
from sqlalchemy.exc import IntegrityError
from server.api import api
from server.database.models import Espaco
from .forms import criar_espaco_parser
from .serializers import espaco_serializer

np_espacos = api.namespace('espacos', description='Espaços de trabalho')


class EspacoResource(Resource):
    """Recursos para o namespace de espaços"""

    @np_espacos.marshal_with(espaco_serializer, code=200)
    def get(self, espaco_id=None):
        """Pega um espaço de trabalho pelo id
        ou todos os espaços de trabalho"""
        if espaco_id:
            espacos = Espaco.query.filter(Espaco.id == str(espaco_id)).first()
            if not espacos:
                abort(404, message='Espaço não encontrado')
        else:
            espacos = Espaco.query.all()
        return espacos, 200

    @np_espacos.expect(criar_espaco_parser, validate=True)
    @np_espacos.marshal_with(espaco_serializer, code=201)
    def post(self):
        """Cria um espaço de trabalho"""
        payload = criar_espaco_parser.parse_args()
        espaco = Espaco()
        espaco.insert_espaco(**payload)
        try:
            espaco.add()
        except IntegrityError:
            espaco.rollback()
            abort(500, message='Erro ao criar um espaço')
        espaco.save()
        return espaco, 201


np_espacos.add_resource(EspacoResource, '/', methods=['POST', 'GET'])
np_espacos.add_resource(EspacoResource, '/<uuid:espaco_id>/', methods=['GET'])
