"""Modelo do espaco de trabalho"""
from .default import DefaultModel, db


class Espaco(DefaultModel):
    """Modelo do espaco de trabalho"""
    __tablename__ = 'Espaco'
    nome = db.Column(db.String(80), nullable=False)
    espaco_de_trabalho_id = db.Column(db.String(36), db.ForeignKey(
        "EspacoDeTrabalho.id"), nullable=False)
    lista = db.relationship("Lista", backref="Espaco")

    membros_espacos = db.relationship(
        "MembroEspaco", backref="Espaco"
    )

    def insert_espaco(self, nome, espaco_de_trabalho_id, **_):
        """Insere o espaco de trabalho"""
        self.nome = nome
        self.espaco_de_trabalho_id = espaco_de_trabalho_id

    def query_with_espaco_trabalho_id(
            self,
            espaco_de_trabalho_id,
            espaco_id=None):
        """Pega um espaco de trabalho pelo id ou levanta 404"""
        query = db.session.query(Espaco).filter(
            Espaco.espaco_de_trabalho_id == espaco_de_trabalho_id,
        )
        if espaco_id:
            return query.filter(
                Espaco.id == espaco_id
            ).first()
        return query.all()
