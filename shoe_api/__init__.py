from flask import Flask

# Config import
from config import Config

# Import for Flask_sqlalchemy and flask_migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

# Instatiate our Database
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from shoe_api import routes, models