"""Modelo de permissao"""
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
