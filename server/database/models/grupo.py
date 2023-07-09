"""Modeloo do Grupo"""
from .default import DefaultModel, db


class Grupo(DefaultModel):
    """Modelo do Grupo"""
    nome = db.Column(db.String(80), nullable=False)

    def insert_grupo(self, nome, **_):
        """Insere o grupo"""
        self.nome = nome
