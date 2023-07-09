"""Modelo do membro"""
from .default import DefaultModel, db


class Membro(DefaultModel):
    """Modelo do membro"""
    __tablename__ = 'Membro'
    usuario_id = db.Column(
        db.String(36),
        db.ForeignKey('Usuario.id'),
        nullable=False)
    espaco_de_trabalho_id = db.Column(
        db.String(36),
        db.ForeignKey('EspacoDeTrabalho.id'),
        nullable=False
    )

    # RELATIONSHIPS
    membro_espacos = db.relationship(
        "MembroEspaco",
        backref="Membro"
    )

    def insert_membro(self, usuario_id, espaco_de_trabalho_id, **_):
        """Insere o membro"""
        self.usuario_id = usuario_id
        self.espaco_de_trabalho_id = espaco_de_trabalho_id
