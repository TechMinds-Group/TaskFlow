"""Modelo do membro"""
from .default import DefaultModel, db


class Membro(DefaultModel):
    """Modelo do membro"""
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'usuario.id'), nullable=False)
    espaco_de_trabalho_id = db.Column(
        db.Integer, db.ForeignKey('espaco_de_trabalho.id'), nullable=False
    )

    def insert_membro(self, usuario_id, espaco_de_trabalho_id, **_):
        """Insere o membro"""
        self.usuario_id = usuario_id
        self.espaco_de_trabalho_id = espaco_de_trabalho_id
