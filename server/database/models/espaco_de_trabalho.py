"""Modelo do espaco de trabalho"""
from .default import DefaultModel, db


class EspacoDeTrabalho(DefaultModel):
    """Modelo do espaco de trabalho"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

    def insert_espaco_de_trabalho(self, nome, **_):
        """Insere o espaco de trabalho"""
        self.nome = nome
