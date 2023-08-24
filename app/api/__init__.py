from flask import Flask, request, jsonify,  Blueprint
import requests
request = requests.get('https://api.open5e.com/')

api = Blueprint("api", __name__)

@api.route("/")
def index():
    return jsonify(request.json())



if __name__ == "__main__":
    pass