from flask import Flask
from flask_material import Material
app = Flask(__name__)
Material(app)
from app import views, model