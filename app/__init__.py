from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#Photo Storage Location

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cihhusqhulpyhk:3363f5e13040908d3f104a7ad068d94d2745096a2097231f9585af964f9ec622@ec2-54-196-111-158.compute-1.amazonaws.com:5432/d7r04rhg7l8g61'
db = SQLAlchemy(app)
app.config.from_object(Config)

from app import views, models