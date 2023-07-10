"""Modelo do membro no grupo"""
from .default import DefaultModel, db


class MembroEspacoGrupo(DefaultModel):
    """Modelo do membro no grupo"""
    __tablename__ = "MembroEspacoGrupo"
    grupo_id = db.Column(
        db.String(36),
        db.ForeignKey("Grupo.id"),
        nullable=False
    )
    membro_espaco_id = db.Column(
        db.String(36),
        db.ForeignKey("MembroEspaco.id"),
        nullable=False
    )

    def insert_membro_grupo(self, grupo_id, membro_espaco_id, **_):
        """Insere o membro no grupo"""
        self.grupo_id = grupo_id
        self.membro_espaco_id = membro_espaco_id
