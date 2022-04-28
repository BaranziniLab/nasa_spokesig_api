import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from nasa_api import db


app = flask.Flask("nasa_spokesig_api", static_folder=None)
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
flask_db = SQLAlchemy(app)




def problem_response(message=None, details=None, status_code=422):
    problem = {}
    problem['message'] = message
    problem['status_code'] = status_code
    if details:
        problem['details'] = details
    return jsonify(problem), status_code


