"""Modelo do membro permissao"""
from .default import DefaultModel, db


class MembroPermissao(DefaultModel):
    """Modelo do membro permissao"""
    membro_espaco_id = db.Column(db.Integer, db.ForeignKey(
        "membro_espaco.id"), nullable=False)
    permissao = db.relationship(
        "Permissao", back_populates="membro_permissao"
    )

    def insert_membro_permissao(self, membro_espaco_id, **_):
        """Insere o membro permissao"""
        self.membro_espaco_id = membro_espaco_id
