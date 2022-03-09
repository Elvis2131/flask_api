from flask import Flask
from flask_mongoengine import MongoEngine
from src.auth_blueprint import auth
from src.bookmark_blueprint import bookmarks
from src.database import db
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(os.environ.get("FLASK_ENV"))
    else:
        app.config.from_mapping(test_config)

    #Registering the various blue prints after declaring the setups.
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    #Setting up the mongoengine connection details.
    app.config['MONGODB_SETTINGS'] = {
        'host': "",
        'connect': False
    }
    db = MongoEngine()
    db.init_app(app)

    @app.get("/")
    def init():
        return {"message":"Hello, you have successfully setup the flask application!"}

    return app