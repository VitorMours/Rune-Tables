from flask import Flask, request, jsonify, render_template, Blueprint

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return render_template("index.jinja")

@views.route("/login")
def login():
    return render_template("login.jinja")

@views.route("/signup")
def signup():
    return render_template("signup.jinja")

