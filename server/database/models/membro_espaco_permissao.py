"""Modelo do membro permissao"""
from .default import DefaultModel, db


class MembroEspacoPermissao(DefaultModel):
    """Modelo do membro permissao"""
    __tablename__ = "MembroEspacoPermissao"
    membro_espaco_id = db.Column(
        db.String(36),
        db.ForeignKey("MembroEspaco.id"),
        nullable=False
    )
    permissao_id = db.Column(
        db.String(36),
        db.ForeignKey("Permissao.id"),
        nullable=False
    )

    def insert_membro_permissao(self, membro_espaco_id, **_):
        """Insere o membro permissao"""
        self.membro_espaco_id = membro_espaco_id
