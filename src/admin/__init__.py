from ..models.user_model import User
from ..extensions import admin, db 
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(User, db.session))
