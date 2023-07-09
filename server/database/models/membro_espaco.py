"""Modelo do membro no espaco de trabalho"""
from .default import DefaultModel, db


class MembroEspaco(DefaultModel):
    """Modelo do membro no espaco de trabalho"""
    espaco_id = db.Column(db.Integer, db.ForeignKey(
        "espaco.id"), nullable=False)
    membro_id = db.Column(db.Integer, db.ForeignKey(
        "membro.id"), nullable=False)

    def insert_membro_espaco(self, espaco_id, membro_id, **_):
        """Insere o membro no espaco de trabalho"""
        self.espaco_id = espaco_id
        self.membro_id = membro_id
