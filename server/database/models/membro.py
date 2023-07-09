"""Modelo do membro"""
from .default import DefaultModel, db


class Membro(DefaultModel):
    """Modelo do membro"""
    usuario_id = db.Column(db.String(36), db.ForeignKey(
        'usuario.id'), nullable=False)
    espaco_de_trabalho_id = db.Column(
        db.String(36), db.ForeignKey('espaco_de_trabalho.id'), nullable=False
    )
    espaco_de_trabalho = db.relationship(
        "EspacoDeTrabalho", back_populates="membro"
    )
    membro_espaco = db.relationship(
        "MembroEspaco", back_populates="membro"
    )

    def insert_membro(self, usuario_id, espaco_de_trabalho_id, **_):
        """Insere o membro"""
        self.usuario_id = usuario_id
        self.espaco_de_trabalho_id = espaco_de_trabalho_id
