from flask import Blueprint
from flask_restful import Api

from .resources import SwaggerView

api_blueprint = Blueprint('api', __name__, url_prefix='/api/{{cookiecutter.api_version}}')

api = Api(api_blueprint)

# Swagger API
api.add_resource(SwaggerView, '/docs', methods=["GET"])
