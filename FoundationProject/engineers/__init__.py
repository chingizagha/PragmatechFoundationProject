from logging import debug
from werkzeug.datastructures import RequestCacheControl
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname, realpath, os
from sqlalchemy.orm import backref
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '12345'
db = SQLAlchemy(app)
from flask_migrate import Migrate
migrate = Migrate(app, db)

from engineers.controllers import *