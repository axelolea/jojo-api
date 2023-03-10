from flask import Flask
from os import environ
from flask_migrate import Migrate

# Database 
from jojo.utils.database import db

# Routes
from jojo.routes.characthers import characters
from jojo.routes.stands import stands
from jojo.routes.parts import parts
from jojo.routes.countries import countries
from jojo.routes.images import images

from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/v1/docs'
API_URL = '/static/swagger.json'

from flask_cors import CORS

swaggerur_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': 'JoJo\' API'
    }
)

def create_app(test_config = None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY'),
            SWAGGER = {
                'title': 'JoJo\'s API',
                'uiversion': 3
            }
        )
    else:
        app.config.from_mapping(test_config)
    
    # Config database
    db.app = app
    db.init_app(app)

    migrate = Migrate(app, db)

    CORS(app)

    app.register_blueprint(characters)
    app.register_blueprint(stands)
    app.register_blueprint(parts)
    app.register_blueprint(countries)
    app.register_blueprint(images)

    # Docs 

    app.register_blueprint(swaggerur_blueprint)

    return app