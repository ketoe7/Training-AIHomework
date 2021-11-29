from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(
    app,
    validate=True,
    doc='/',
    title='An API for checking connectivity',
    description='Sample description',
    contact='mikolaj.wierzbicki1@gmail.com',
    version="1.0"
)

from app import routes
