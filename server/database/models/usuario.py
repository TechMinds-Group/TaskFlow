"""Modelo do usuario"""
from werkzeug.security import generate_password_hash, check_password_hash
from .default import DefaultModel, db


class Usuario(DefaultModel):
    """Modelo do usuario"""
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    membros = db.relationship("Membro", backref="usuario", lazy=True)

    def set_password(self, password):
        """Define a senha do usuario criptografada"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a senha informada é a mesma do usuario"""
        return check_password_hash(self.password, password)

    def insert_credentials(self, username, password, **_):
        """Insere as credenciais do usuario"""
        self.username = username
        self.set_password(password)

    def insert_perfil(self, nome, **_):
        """Insere o perfil do usuario"""
        self.nome = nome
