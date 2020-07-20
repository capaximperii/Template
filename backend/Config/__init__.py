import os
import socket
import requests

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Make sure our CWD is predictable.
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'Thisissupposedtobesecret'
    SERVER_ADDRESS = get_ip_address()
    GOOGLE_SECRET = 'Xxg7wP76j0N2sU-aiSMAVuNw'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI =  'mssql+pyodbc://production:simulation@123@10.206.246.184/StmMatch?driver=SQL+Server'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Data/statmatch.db?check_same_thread=False&timeout=5'

class TestingConfig(Config):
    TESTING = True

def initialize(appl):
    if os.environ.get('FLASK_ENV', None) == 'production':
        print('Loading production config')
        appl.config.from_object(ProductionConfig)
    else:
        print('Loading development config')
        appl.config.from_object(DevelopmentConfig)