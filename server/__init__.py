"""Módulo de inicialização do servidor"""
from importlib import import_module
from flask import Flask
import click


class Servidor(Flask):
    """Classe de inicialização do servidor"""
    init_db = import_module('server.database').init_app
    init_api = import_module('server.api').init_app

    def __init__(self):
        super().__init__(__name__)
        self.config.from_prefixed_env()
        self.db = None  # pylint: disable=invalid-name
        self.api = None  # pylint: disable=invalid-name

    def create_database(self):
        """Cria o banco de dados"""
        with self.app_context():
            self.db.create_all()

    def commands(self):
        """Adiciona os comandos ao servidor"""
        self.cli.add_command(
            # pylint: disable=unnecessary-lambda
            cmd=click.command(lambda: self.create_database()),
            name='create_database'
        )

    def setup(self):
        """Inicializa o servidor"""
        with self.app_context():
            self.db = self.init_db()
            self.api = self.init_api()
            self.commands()
