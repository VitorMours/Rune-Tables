from ..models.user_model import User
import json
from ..extensions import db
class UserRepository:

    def create(self, user: User) -> User: 
        db.session.add(user)
        db.session.commit()
        return user

    def find_all(self) -> json:
        return User.query.all() 

    def count(self) -> int:
        return User.query.count()

    def find_by_email(self, email: str) -> User | None:
        if user := User.query.filter_by(email=email).first():
            return user
        return False

    def delete(self) -> None:
        pass 
    
    def update(self) -> None: 
        pass 
    
    def get(self) -> None:
        pass 
    
