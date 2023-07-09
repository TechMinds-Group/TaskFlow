"""Controle de usuário"""
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class UsuarioControl():
    """Classe de controle de usuário"""

    def generate_token(self):
        """Gera um token de autenticação"""
        return create_access_token(
            identity=self.id  # pylint: disable=no-member
        )

    def check_password(self, password):
        """Verifica se a senha informada é a mesma do usuario"""
        return check_password_hash(
            self.password, password  # pylint: disable=no-member
        )
