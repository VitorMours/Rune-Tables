from src import create_app
import os 

if __name__ == "__main__":
  app = create_app()
  os.environ.setdefault("FLASK_APP","src/__init__.py")
  app.run()