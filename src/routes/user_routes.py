from flask_restx import Namespace, fields, Resource, abort
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService 

ns = Namespace("user", description="User namespace related")

user_repository = UserRepository()
user_service = UserService(user_repository)


user_model = ns.model("User", {
    "id": fields.String(readonly=True),
    "name": fields.String(description="User name"),
    "surname": fields.String(description="User surname"),
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

@ns.route("/")
class User(Resource):
    """User related resource, to update, access, delete or create."""

    def get(self):
        quantity, user_json = user_service.get_all() 
        return {"quantity":quantity, "users": user_json}

    @ns.expect(user_model)
    def post(self) :
        user_json = ns.payload 
        if user := user_service.register_user(user_json):
            return {"user": user.to_json()}, 201
        return None

    def put(self):
        pass
