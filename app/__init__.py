from flask import Flask, jsonify, request, Blueprint
from .views import views
from .auth import auth
from .api import api


def run_app():
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")

    app.run(debug=True)
