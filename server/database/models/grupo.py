"""Modeloo do Grupo"""
from .default import DefaultModel, db


class Grupo(DefaultModel):
    """Modelo do Grupo"""
    nome = db.Column(db.String(80), nullable=False)
    grupo_permissao = db.relationship("GrupoPermissao", backref="grupo")

    def insert_grupo(self, nome, **_):
        """Insere o grupo"""
        self.nome = nome
