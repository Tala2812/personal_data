from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_very_secret_key'

from app import routes