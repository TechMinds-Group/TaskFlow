"""Modelo do espaco de trabalho"""
from .default import DefaultModel, db


class EspacoDeTrabalho(DefaultModel):
    """Modelo do espaco de trabalho"""
    nome = db.Column(db.String(80), nullable=False)
    espaco = db.relationship("Espaco", backref="espaco_de_trabalho")

    def insert_espaco_de_trabalho(self, nome, **_):
        """Insere o espaco de trabalho"""
        self.nome = nome
