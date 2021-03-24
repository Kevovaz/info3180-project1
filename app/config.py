import os

class Config(object):
	"""Base Config Object"""
	DEBUG = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://cihhusqhulpyhk:3363f5e13040908d3f104a7ad068d94d2745096a2097231f9585af964f9ec622@ec2-54-196-111-158.compute-1.amazonaws.com:5432/d7r04rhg7l8g61'
	SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
	UPLOAD_FOLDER = 'app/static/uploads/'
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
