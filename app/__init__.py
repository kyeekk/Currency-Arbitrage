from flask import Flask
SECRET_KEY = 'Sup3r$3cretkey'
app = Flask(__name__)
from app import views
