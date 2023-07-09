"""Modeloo do Grupo"""
from .default import DefaultModel, db


class Grupo(DefaultModel):
    """Modelo do Grupo"""
    __tablename__ = "Grupo"
    nome = db.Column(db.String(80), nullable=False)

    # RELATIONSHIPS
    grupo_permissoes = db.relationship(
        "GrupoPermissao",
        backref="Grupo",
        lazy=True
    )
    membro_espaco_grupos = db.relationship(
        "MembroEspacoGrupo",
        backref="Grupo",
        lazy=True
    )

    def insert_grupo(self, nome, **_):
        """Insere o grupo"""
        self.nome = nome
