import flask
from nasa_api import db
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask("nasa_spokesig_api", static_folder=None)
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flask_db = SQLAlchemy(app)