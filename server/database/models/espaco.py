"""Modelo do espaco de trabalho"""
from .default import DefaultModel, db


class Espaco(DefaultModel):
    """Modelo do espaco de trabalho"""
    nome = db.Column(db.String(80), nullable=False)
    espaco_de_trabalho_id = db.Column(db.Integer, db.ForeignKey(
        "espaco_de_trabalho.id"), nullable=False)

    def insert_espaco(self, nome, espaco_de_trabalho_id, **_):
        """Insere o espaco de trabalho"""
        self.nome = nome
        self.espaco_de_trabalho_id = espaco_de_trabalho_id
