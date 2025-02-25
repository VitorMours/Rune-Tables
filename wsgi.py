from src import create_app, db
from flask_migrate import Migrate


if __name__ == "__main__":
    app = create_app()
    Migrate(app, db)
    app.run()
