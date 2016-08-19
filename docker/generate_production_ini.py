# coding: utf-8
import os
from configparser import ConfigParser

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
production_template_ini_filepath = os.path.join(PROJECT_PATH + '/production.ini-TEMPLATE')
new_production_ini_filepath = os.path.join(PROJECT_PATH + '/production.ini')
config = ConfigParser()
config.read_file(open(production_template_ini_filepath))
config.set('app:main', 'elasticsearch', os.environ.get('ELASTICSEARCH', '127.0.0.1:9200'))
config.set('app:main', 'articlemeta', os.environ.get('ARTICLEMETA', 'articlemeta.scielo.org:11720'))
config.set('server:main', 'port', '8000')

with open(new_production_ini_filepath, 'w') as configfile:
    config.write(configfile)
