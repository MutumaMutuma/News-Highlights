from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
# Initializing application
app = Flask(__name__)

from app import views
