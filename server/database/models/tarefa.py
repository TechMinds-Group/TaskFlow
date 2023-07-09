"""Modelo de tarefa"""
from .default import DefaultModel, db


class Tarefa(DefaultModel):
    """Modelo de tarefa"""
    nome = db.Column(db.String(80), nullable=False)
    tarefa_id = db.Column(db.Integer, db.ForeignKey(
        "tarefa.id"), nullable=False)
    lista_id = db.Column(db.Integer, db.ForeignKey(
        "lista.id"), nullable=False)
    menssagem = db.relationship("Mensagem", backref="tarefa")

    def insert_tarefa(self, nome, tarefa_id, lista_id, **_):
        """Insere a tarefa"""
        self.nome = nome
        self.tarefa_id = tarefa_id
        self.lista_id = lista_id
