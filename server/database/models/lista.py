"""Modelos de lista"""
from .default import DefaultModel, db


class Lista(DefaultModel):
    """Modelo de lista"""
    nome = db.Column(db.String(80), nullable=False)
    espaco_id = db.Column(db.Integer, db.ForeignKey(
        "espaco.id"), nullable=False)
    tarefa = db.relationship("Tarefa", backref="lista")

    def insert_lista(self, nome, espaco_id, **_):
        """Insere a lista"""
        self.nome = nome
        self.espaco_id = espaco_id
