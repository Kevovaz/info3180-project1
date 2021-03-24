from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#Photo Storage Location

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kfakoaxmcofchc:29bb9b3871d53420170240f098e34b7321e15d0de85ffec5a8bc4ce10ce0b984@ec2-54-161-239-198.compute-1.amazonaws.com:5432/davk2k4d1i5m19'
db = SQLAlchemy(app)
app.config.from_object(Config)

from app import views, models