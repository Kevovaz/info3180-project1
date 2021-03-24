from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

#Photo Storage Location

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Som3$ec5etK*y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cnneedlquvdmhq:e2854ebd6c69f303e7e55c2d0db5f2073680bf73d90a57cf0e98132f244c88b6@ec2-54-164-22-242.compute-1.amazonaws.com:5432/dc8sj47hchbrdc'
db = SQLAlchemy(app)
app.config.from_object(Config)

from app import views, models