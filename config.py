import os 

BASE_DIR = os.path.dirname(__file__)



# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql://ehddy:4631@172.17.0.4:5432/flask_db'

SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = "dev"