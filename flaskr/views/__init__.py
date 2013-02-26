from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.googleauth import (GoogleFederated, GoogleAuth)

app = Flask(__name__)
app.config.from_object('flaskr.config')
db = SQLAlchemy(app)

auth = GoogleAuth(app)
