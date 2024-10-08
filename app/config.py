import os
import uuid


class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', '')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
    HOST = os.environ.get('POSTGRES_HOST', '')
    PORT = os.environ.get('POSTGRES_PORT', '')
    DB = os.environ.get('POSTGRES_DB', '')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'aivoobiec7aeshahga1naesahth5aCi2oe7quah1'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
