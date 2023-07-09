"""Modelo de subtarefa"""
from .default import DefaultModel, db


class Subtarefa(DefaultModel):
    """Modelo de subtarefa"""
    parent_tarefa_id = db.Column(db.String(36), db.ForeignKey(
        "parent_tarefa.id"), nullable=False)
    tarefa_id = db.Column(db.String(36), db.ForeignKey(
        "tarefa.id"), nullable=False)
    tarefa = db.relationship(
        "Tarefa",
        primaryjoin="and_(Subtarefa.parent_tarefa_id == Tarefa.parent_id, "
                    "Subtarefa.tarefa_id == Tarefa.id)",
        backref="subtarefa"
    )

    def insert_subtarefa(self, parent_tarefa_id, tarefa_id, **_):
        """Insere a subtarefa"""
        self.parent_tarefa_id = parent_tarefa_id
        self.tarefa_id = tarefa_id
