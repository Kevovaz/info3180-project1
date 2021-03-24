from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#Photo Storage Location

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proj1:password@localhost/proj1'
db = SQLAlchemy(app)
app.config.from_object(Config)

from app import views, models