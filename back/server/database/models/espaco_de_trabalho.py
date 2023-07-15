"""Modelo do espaco de trabalho"""
from sqlalchemy import and_
from loguru import logger
from .default import DefaultModel, db
from .membro import Membro


class EspacoDeTrabalho(DefaultModel):
    """Modelo do espaco de trabalho"""
    __tablename__ = "EspacoDeTrabalho"
    nome = db.Column(
        db.String(80),
        nullable=False
    )

    # RELATIONSHIPS
    espacos = db.relationship(
        "Espaco",
        backref="EspacoDeTrabalho",
        lazy=True
    )
    membros = db.relationship(
        "Membro",
        backref="EspacoDeTrabalho",
        lazy=True
    )

    def insert_espaco_de_trabalho(self, nome, **_):
        """Insere o espaco de trabalho"""
        self.nome = nome

    @staticmethod
    def query_with_user(usuario_id, espaco_de_trabalho_id=None):
        """Pega um espaco de trabalho pelo id ou levanta 404"""
        query = db.session.query(EspacoDeTrabalho).join(
            Membro, and_(
                Membro.usuario_id == usuario_id,
                EspacoDeTrabalho.id == Membro.espaco_de_trabalho_id
            )
        )
        if espaco_de_trabalho_id:
            query = query.filter(
                EspacoDeTrabalho.id == espaco_de_trabalho_id
            ).first()
        else:
            query = query.all()
        return query

    def add_membro(self, usuario_id):
        """Adiciona um membro ao espaco de trabalho"""
        logger.debug(f'🤖 Adicionando membro {usuario_id} '
                     f'ao espaco de trabalho {self.id}')
        membro = Membro.query.filter(
            Membro.usuario_id == usuario_id,
            Membro.espaco_de_trabalho_id == self.id
        ).first()
        if membro:
            return membro

        membro = Membro()
        membro.insert_membro(
            usuario_id=usuario_id,
            espaco_de_trabalho_id=self.id
        )
        membro.add()
        return membro
