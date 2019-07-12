import os

DIALECT = 'mysql'
USER = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
DATABASE = 'flask_sql_demo'

SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(DIALECT, USER, PASSWORD, HOST, DATABASE)

# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/flask_sql_demo'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)

DEBUG = True
