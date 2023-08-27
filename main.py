import sys

if __name__ == "__main__":
    match sys.argv[1]:
        case "web":
            import app
            app.run_app()

        case "api":
            from app.api import creator
            usuario = creator.CharacterCreator({"name": "Jonilson", "age":22})
            print(usuario.__dict__)

        case "total":
            import app
            from app import api

            usuario = api.CharacterCreator()
            print(usuario)

            app.run_app(debug=True)
