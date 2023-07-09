"""Modelo do grupo permissao"""
from .default import DefaultModel, db


class GrupoPermissao(DefaultModel):
    """Modelo do grupo permissao"""
    __tablename__ = "GrupoPermissao"
    permissao_id = db.Column(db.String(36), db.ForeignKey(
        "Permissao.id"), nullable=False)
    grupo_id = db.Column(db.String(36), db.ForeignKey(
        "Grupo.id"), nullable=False)

    def insert_grupo_permissao(self, permissao_id, grupo_id, **_):
        """Insere o grupo permissao"""
        self.permissao_id = permissao_id
        self.grupo_id = grupo_id
