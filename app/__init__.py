from flask import Flask
# THESE WERE ADDED
from flask_mail import Mail
from .config import Config
#
app = Flask(__name__)

# THESE WERE ADDED
app.config.from_object(Config) 
mail = Mail(app)
#

from app import views