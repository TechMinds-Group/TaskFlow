from flask import Flask


class Servidor(Flask):
    def __init__(self):
        super().__init__(__name__)
