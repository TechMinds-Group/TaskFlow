"""Modeloo do Grupo"""
from loguru import logger
from .default import DefaultModel, db
from .grupo_permissao import GrupoPermissao


class Grupo(DefaultModel):
    """Modelo do Grupo"""
    __tablename__ = "Grupo"
    nome = db.Column(
        db.String(255),
        nullable=False
    )
    customizar = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    # RELATIONSHIPS
    grupo_permissoes = db.relationship(
        "GrupoPermissao",
        backref="Grupo",
        lazy=True
    )
    membro_espaco_grupos = db.relationship(
        "MembroEspacoGrupo",
        backref="Grupo",
        lazy=True
    )

    def insert_grupo(self, nome, customizar, **_):
        """Insere o grupo"""
        self.nome = nome
        self.customizar = customizar

    @staticmethod
    def create_grupo_with_permissions(endpoint, permissions: list = None):
        """Cria o grupo"""
        permissions = permissions or []
        grupo = Grupo.query.filter(
            Grupo.nome == endpoint,
            Grupo.customizar == False  # noqa # pylint: disable=singleton-comparison
        ).first()
        if not grupo:
            logger.debug(
                f'🤖 Novo Grupos de permissões no sistema endpoint:{endpoint}'
            )
            grupo = Grupo()
            grupo.insert_grupo(
                nome=endpoint,
                customizar=False
            )
            grupo.add()
        for permission in permissions:
            grupo.add_permission(permission.id)
        return grupo

    def add_permission(self, permissao_id):
        """Adiciona uma permissao ao grupo"""
        grupo_permissao = GrupoPermissao.query.filter(
            GrupoPermissao.grupo_id == self.id,
            GrupoPermissao.permissao_id == permissao_id
        ).first()
        if not grupo_permissao:
            grupo_permissao = GrupoPermissao()
            grupo_permissao.insert_grupo_permissao(
                permissao_id=permissao_id,
                grupo_id=self.id
            )
            grupo_permissao.add()
        return grupo_permissao
