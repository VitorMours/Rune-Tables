from flask_sqlalchemy import SQLAlchemy 
from flask_admin import Admin 


admin = Admin(template_mode="bootstrap3", name="Rune Tables")

db = SQLAlchemy()