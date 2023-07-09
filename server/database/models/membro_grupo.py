"""Modelo do membro no grupo"""
from .default import DefaultModel, db


class MembroGrupo(DefaultModel):
    """Modelo do membro no grupo"""
    grupo_id = db.Column(db.Integer, db.ForeignKey(
        "grupo.id"), nullable=False)
    membro_espaco_id = db.Column(db.Integer, db.ForeignKey(
        "membro_espaco.id"), nullable=False)
    grupo = db.relationship(
        "Grupo", back_populates="membro_grupo"
    )

    def insert_membro_grupo(self, grupo_id, membro_espaco_id, **_):
        """Insere o membro no grupo"""
        self.grupo_id = grupo_id
        self.membro_espaco_id = membro_espaco_id
