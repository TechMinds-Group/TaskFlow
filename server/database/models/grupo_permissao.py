"""Modelo do grupo permissao"""
from .default import DefaultModel, db


class GrupoPermissao(DefaultModel):
    """Modelo do grupo permissao"""
    permissao_id = db.Column(db.Integer, db.ForeignKey(
        "permissao.id"), nullable=False)
    grupo_id = db.Column(db.Integer, db.ForeignKey(
        "grupo.id"), nullable=False)
    permissao = db.relationship(
        "Permissao", back_populates="grupo_permissao"
    )

    def insert_grupo_permissao(self, permissao_id, grupo_id, **_):
        """Insere o grupo permissao"""
        self.permissao_id = permissao_id
        self.grupo_id = grupo_id
