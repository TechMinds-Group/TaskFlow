"""Modelo do membro no espaco de trabalho"""
from .default import DefaultModel, db


class MembroEspaco(DefaultModel):
    """Modelo do membro no espaco de trabalho"""
    espaco_id = db.Column(db.String(36), db.ForeignKey(
        "espaco.id"), nullable=False)
    membro_id = db.Column(db.String(36), db.ForeignKey(
        "membro.id"), nullable=False)
    membro_permissao = db.relationship(
        "MembroPermissao", back_populates="membro_espaco"
    )
    membro_grupo = db.relationship(
        "MembroGrupo", back_populates="membro_espaco"
    )

    def insert_membro_espaco(self, espaco_id, membro_id, **_):
        """Insere o membro no espaco de trabalho"""
        self.espaco_id = espaco_id
        self.membro_id = membro_id
