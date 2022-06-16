# These details can be stored in env variables

import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(basedir, 'iot.sqlite3')
db_path = 'sqlite:///' + os.path.join(basedir, 'iot.sqlite3')

secrete_key = "True"

# Value in seconds
jwt_access_expires = 600