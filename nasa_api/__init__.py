import flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from nasa_api import db

app_name = "nasa_spokesig_api"
app = flask.Flask(app_name)

# app configs
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

# swagger configs
SWAGGER_URL = "/nasa_api/v1/swagger"
API_URL = "/static/swagger.yaml"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name" : app_name
    }
)
app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
    
flask_db = SQLAlchemy(app)

def problem_response(message=None, details=None, status_code=422):
    problem = {}
    problem['message'] = message
    problem['status_code'] = status_code
    if details:
        problem['details'] = details
    return jsonify(problem), status_code


