from flask import Flask

import sys

import sys
import os
# import torch.backends.cudnn as cudnn
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from configparser import ConfigParser
#from controllers.find_plants import plants
#from controllers.get_diseases import diseases
from controllers.get_scientific_name import scientific_name
#from controllers.insert_records_into_db import insert_records
#from database.database_connection import db

app = Flask(__name__)

# Register the blueprint from the controller
#app.register_blueprint(plants)
#app.register_blueprint(diseases)
app.register_blueprint(scientific_name)
#app.register_blueprint(insert_records)

'''config = ConfigParser()
config.read('config.ini')

db_user = config.get('database', 'user')
db_password = config.get('database', 'password')
db_host = config.get('database', 'host')
db_name = config.get('database', 'database_name')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
'''
if __name__ == "__main__":
    app.run(debug=True)
