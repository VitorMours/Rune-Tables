from flask import Flask 
from flask_restx import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy 
from flask_admin.contrib.sqla import ModelView
from .models.user_model import User
from .extensions import db, admin
from .routes import api

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///development.sqlite3"
    app.config['FLASK_ADMIN_SWATCH'] = 'lumen'
    CORS(app)

    db.init_app(app)
    admin.init_app(app)
    api.init_app(app)
    # app.register_blueprint(api, url_prefix="/api")

    
    # Adding Administrative views
    admin.add_view(ModelView(User, db.session))

    with app.app_context():
        db.create_all()

    return app 


if __name__ == "__main__":
    app = create_app()
    app.run()
