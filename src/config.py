# To change this template, choose Tools | Templates
# and open the template in the editor.
# CONFIGURACION DEL PROYECTO
import os
DEBUG = True

_basedir = os.path.abspath(os.path.dirname(__file__))
WHOOSH_BASE = os.path.join(_basedir, 'search.db')
DATA_PATH = os.path.join(_basedir, 'data')
DEFAULT_TPL = 'static'

SECRET_KEY = 'secret devel key'

URL = 'http://localhost:8080/'
TITLE = 'Proyecto SICP'
VERSION = '0.1'
LANG = 'es'
LANG_DIRECTION = 'ltr'
YEAR = '2013'

SQLALCHEMY_DATABASE_URI = 'postgresql://administrador:admin@localhost:5432/basedatos'
#SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost:5432/databasePrueba'


del os


