"""Modelo de subtarefa"""
from .default import DefaultModel, db


class Subtarefa(DefaultModel):
    """Modelo de subtarefa"""
    __tablename__ = "Subtarefa"
    parent_tarefa_id = db.Column(
        db.String(36),
        db.ForeignKey("Tarefa.id"),
        nullable=False)
    tarefa_id = db.Column(
        db.String(36),
        db.ForeignKey("Tarefa.id"),
        nullable=False
    )

    # RELATIONSHIPS
    parent_subtasks = db.relationship(
        'Tarefa',
        foreign_keys=[parent_tarefa_id]
    )
    subtasks = db.relationship(
        'Tarefa',
        foreign_keys=[tarefa_id]
    )

    def insert_subtarefa(self, parent_tarefa_id, tarefa_id, **_):
        """Insere a subtarefa"""
        self.parent_tarefa_id = parent_tarefa_id
        self.tarefa_id = tarefa_id
