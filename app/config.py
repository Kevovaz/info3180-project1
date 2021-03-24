import os

class Config(object):
	"""Base Config Object"""
	DEBUG = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://cnneedlquvdmhq:e2854ebd6c69f303e7e55c2d0db5f2073680bf73d90a57cf0e98132f244c88b6@ec2-54-164-22-242.compute-1.amazonaws.com:5432/dc8sj47hchbrdc'
	SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
	UPLOAD_FOLDER = 'app/static/uploads/'
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
