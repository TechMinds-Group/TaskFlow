"""Modelo de tarefa"""
from .default import DefaultModel, db


class Tarefa(DefaultModel):
    """Modelo de tarefa"""
    __tablename__ = "Tarefa"
    nome = db.Column(
        db.String(80),
        nullable=False
    )
    lista_id = db.Column(
        db.String(36),
        db.ForeignKey("Lista.id"),
        nullable=False
    )

    # RELATIONSHIPS
    menssagem = db.relationship(
        "Mensagem",
        backref="tarefa",
        lazy=True
    )

    def insert_tarefa(self, nome, lista_id, **_):
        """Insere a tarefa"""
        self.nome = nome
        self.lista_id = lista_id
