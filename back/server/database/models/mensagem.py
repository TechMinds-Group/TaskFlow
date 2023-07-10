"""Modelo de mensagem"""
from .default import DefaultModel, db


class Mensagem(DefaultModel):
    """Modelo de mensagem"""
    __tablename__ = "Mensagem"
    membro_id = db.Column(
        db.String(36),
        db.ForeignKey("Membro.id"),
        nullable=False)
    tarefa_id = db.Column(
        db.String(36),
        db.ForeignKey("Tarefa.id"),
        nullable=False)

    def insert_mensagem(self, membro_id, tarefa_id, **_):
        """Insere a mensagem"""
        self.membro_id = membro_id
        self.tarefa_id = tarefa_id
