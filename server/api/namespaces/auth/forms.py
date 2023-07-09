"""Forms do namespace auth."""
from flask_restx.reqparse import RequestParser


login_parser = RequestParser()
form = login_parser
form.add_argument(
    'username',
    required=True,
    location='json',
)
form.add_argument(
    'password',
    required=True,
    location='json',
)
