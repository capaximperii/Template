from flask import Flask
from waitress import serve
from flask_cors import CORS
from flask_gzip import Gzip
import Config
import Models
import Controllers
import Authentication
import Workers

app = Flask(__name__, static_url_path='', static_folder='./Ui')
CORS(app, resources={r'/*': {'origins': '*'}})
Gzip(app)
Config.initialize(app)
Controllers.initialize(app)
Models.initialize(app)
Authentication.initialize(app)
Workers.initialize(app)
# print(app.url_map)


if __name__=='__main__':
    print(f'Listening on all interfaces on port 8888')
    serve(app, host='0.0.0.0', port=8888)
