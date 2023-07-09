from flask import Flask
from importlib import import_module


class Servidor(Flask):
    init_db = import_module('server.database').init_app

    def __init__(self):
        super().__init__(__name__)
        self.config.from_prefixed_env()

    def setup(self):
        self.db = self.init_db()