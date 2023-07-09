"""Modelo do membro no espaco de trabalho"""
from .default import DefaultModel, db


class MembroEspaco(DefaultModel):
    """Modelo do membro no espaco de trabalho"""
    __tablename__ = "MembroEspaco"
    espaco_id = db.Column(
        db.String(36),
        db.ForeignKey("Espaco.id"),
        nullable=False
    )
    membro_id = db.Column(
        db.String(36),
        db.ForeignKey("Membro.id"),
        nullable=False)

    # RELATIONSHIPS
    membro_permissoes = db.relationship(
        "MembroEspacoPermissao",
        backref="MembroEspaco"
    )
    membro_espacos_grupos = db.relationship(
        "MembroEspacoGrupo",
        backref="MembroEspaco"
    )

    def insert_membro_espaco(self, espaco_id, membro_id, **_):
        """Insere o membro no espaco de trabalho"""
        self.espaco_id = espaco_id
        self.membro_id = membro_id
