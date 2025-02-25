from flask_restx import Namespace, fields, Resource 



ns = Namespace("user", description="User namespace related")

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
        return True 

    def post(self):
        pass 

    def put(self):
        pass
