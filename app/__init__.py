from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
lm= LoginManager(app)



from app import views, model
