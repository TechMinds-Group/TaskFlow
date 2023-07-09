from flask import Flask
from importlib import import_module
import click


class Servidor(Flask):
    init_db = import_module('server.database').init_app

    def __init__(self):
        super().__init__(__name__)
        self.config.from_prefixed_env()

    def create_database(self):
        """Cria o banco de dados"""
        with self.app_context():
            self.db.create_all()

    def commands(self):
        """Adiciona os comandos ao servidor"""
        self.cli.add_command(
            cmd=click.command(lambda: self.create_database()),
            name='create_database'
        )

    def setup(self):
        """Inicializa o servidor"""
        with self.app_context():
            self.db = self.init_db()
            self.commands()
