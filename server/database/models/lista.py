"""Modelos de lista"""
from .default import DefaultModel, db


class Lista(DefaultModel):
    """Modelo de lista"""
    __tablename__ = "Lista"
    nome = db.Column(db.String(80), nullable=False)
    espaco_id = db.Column(db.String(36), db.ForeignKey(
        "Espaco.id"), nullable=False)

    # RELATIONSHIPS
    tarefas = db.relationship(
        "Tarefa",
        backref="Lista",
        lazy=True
    )

    def insert_lista(self, nome, espaco_id, **_):
        """Insere a lista"""
        self.nome = nome
        self.espaco_id = espaco_id
