# pylint: disable=missing-module-docstring
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Good'
