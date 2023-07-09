"""Módulo base para os modelos"""
from uuid import uuid4
from .. import db


class DefaultModel(db.Model):
    """Classe base para os modelos"""
    __abstract__ = True
    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid4()))
    excluido = db.Column(db.Boolean, default=False)
    ativo = db.Column(db.Boolean, default=True)
    data_criado = db.Column(
        db.DateTime,
        default=db.func.now()
    )
    data_atualizado = db.Column(
        db.DateTime,
        default=db.func.now(),
        onupdate=db.func.now()
    )

    def add(self):
        """Adiciona o objeto ao banco de dados"""
        db.session.add(self)
        db.session.flush()
        return self

    def save(self):
        """Salva o objeto no banco de dados"""
        db.session.commit()
        return self

    def delete(self):
        """Remove o objeto do banco de dados"""
        db.session.delete(self)
        return self
