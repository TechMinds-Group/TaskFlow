"""Modelo do usuario"""
from werkzeug.security import generate_password_hash
from ..controls import UsuarioControl
from .default import DefaultModel, db


class Usuario(DefaultModel, UsuarioControl):
    """Modelo do usuario"""
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(80), nullable=False)

    def insert_password(self, password):
        """Define a senha do usuario criptografada"""
        self.password = generate_password_hash(password)

    def insert_credentials(self, username, password, **_):
        """Insere as credenciais do usuario"""
        self.username = username
        self.insert_password(password)

    def insert_perfil(self, nome, **_):
        """Insere o perfil do usuario"""
        self.nome = nome
