import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from .models import db
from .api import api_blueprint

# Example for commands imports
# from .commands import create_superadmin


load_dotenv()


def create_app(testing=False):
    app = Flask('{{cookiecutter.project_name}}_api')

    config_path = os.getenv("{{cookiecutter.project_name_uppercase}}_API_CONFIG_PATH", "{{cookiecutter.project_name}}_api.config.LocalConfig")
    app.config.from_object(config_path)

    if testing is True:
        app.config['TESTING'] = True

    CORS(app)

    # Init db extension
    db.init_app(app)

    app.register_blueprint(api_blueprint)

    # Register general commands
    # app.cli.add_command(create_superadmin)
    return app
