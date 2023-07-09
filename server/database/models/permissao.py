"""Modelo de permissao"""
from loguru import logger
from .default import DefaultModel, db


class Permissao(DefaultModel):
    """Modelo de permissao"""
    __tablename__ = "Permissao"
    endpoint = db.Column(
        db.String(80),
        nullable=False
    )
    metodo = db.Column(
        db.String(80),
        nullable=False
    )
    customizar = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    grupo_permissoes = db.relationship(
        "GrupoPermissao",
        backref="Permissao",
        lazy=True
    )
    membros_espaco_permissoes = db.relationship(
        "MembroEspacoPermissao",
        backref="Permissao",
        lazy=True
    )

    def insert_permissao(self, endpoint, metodo, customizar, **_):
        """Insere a permissao"""
        self.endpoint = endpoint
        self.metodo = metodo
        self.customizar = customizar

    @staticmethod
    def reset_permissions():
        """Reseta as permissões de uma rota colocando todas como excluídas"""
        logger.debug('🤖 Reiniciando as permissões.')
        db.session.query(Permissao).filter(
            Permissao.customizar == False  # noqa # pylint: disable=singleton-comparison
        ).update({
            'excluido': True
        })
        db.session.commit()

    @staticmethod
    def add_permissao(endpoint, method):
        """Adiciona uma permissao"""
        logger.debug('🤖 Nova Permissão no sistema'
                     f' endpoint:{endpoint} method:{method}.')
        permissao = Permissao()
        permissao.insert_permissao(
            endpoint=endpoint,
            metodo=method,
            customizar=False,
            excluido=False
        )
        permissao.add()
        return permissao

    @staticmethod
    def create_permissions(endpoint, methods):
        """Cria as permissões de rotas do servidor"""
        for method in methods:
            permissao = Permissao.query.filter(
                Permissao.endpoint == endpoint,
                Permissao.metodo == method,
                Permissao.customizar == False  # noqa # pylint: disable=singleton-comparison
            ).first()
            if permissao is None:
                permissao = Permissao.add_permissao(
                    endpoint=endpoint,
                    method=method
                )
            else:
                permissao.customizar = False
                permissao.excluido = False
        permissao.save()
