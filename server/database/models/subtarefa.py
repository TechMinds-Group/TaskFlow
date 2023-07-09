"""Modelo de subtarefa"""
from .default import DefaultModel, db


class Subtarefa(DefaultModel):
    """Modelo de subtarefa"""
    parent_tarefa_id = db.Column(db.String(36), db.ForeignKey(
        "tarefa.id"), nullable=False)
    tarefa_id = db.Column(db.String(36), db.ForeignKey(
        "tarefa.id"), nullable=False)

    parent_subtasks = db.relationship(
        'tarefa', foreign_keys=[parent_tarefa_id])
    subtasks = db.relationship('tarefa', foreign_keys=[tarefa_id])

    def insert_subtarefa(self, parent_tarefa_id, tarefa_id, **_):
        """Insere a subtarefa"""
        self.parent_tarefa_id = parent_tarefa_id
        self.tarefa_id = tarefa_id
