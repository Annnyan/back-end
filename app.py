from flask_smorest import Api
from resources.user import blp as UserBlueprint
from resources.category import blp as CategoryBlueprint
from resources.record import blp as RecordBlueprint
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Backend app"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(RecordBlueprint)

    return app
