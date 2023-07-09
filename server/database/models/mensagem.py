"""Modelo de mensagem"""
from .default import DefaultModel, db


class Mensagem(DefaultModel):
    """Modelo de mensagem"""
    membro_id = db.Column(db.Integer, db.ForeignKey(
        "membro.id"), nullable=False)
    tarefa_id = db.Column(db.Integer, db.ForeignKey(
        "tarefa.id"), nullable=False)

    def insert_mensagem(self, membro_id, tarefa_id, **_):
        """Insere a mensagem"""
        self.membro_id = membro_id
        self.tarefa_id = tarefa_id
