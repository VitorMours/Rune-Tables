from ..repositories.user_repository import UserRepository
from ..models.user_model import User, UserSchema
import json
from flask_restx import abort

class UserService:

    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register_user(self, user_json) -> None:
        user_schema = UserSchema(**user_json)
        new_user = User(**user_schema.model_dump())
        new_user.password = user_schema.password.get_secret_value()
        
        if user := self.user_repository.find_by_email(new_user.email):        
            return abort(400, message=f"You cannot create the user because already exists in the database"), 
        else:
            return self.user_repository.create(new_user)

    def get_all(self) -> None:
        users = self.user_repository.find_all()
        quantity = self.user_repository.count()
        
        return quantity, [user_register.to_json() for user_register in users] 
