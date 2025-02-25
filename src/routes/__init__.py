from flask_restx import Api 
from .user_routes import ns as user


api = Api(title="Rune Tables Back-End", version="0.0.1", description="Runetables back end")

api.add_namespace(user)