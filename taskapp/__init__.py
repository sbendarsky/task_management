from flask import Flask, render_template
from pymongo import MongoClient
from taskapp.views import taskapp


def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    # MongoDB configuration
    app.config["MONGO_URI"] = "mongodb://localhost:27017/taskapp"
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.taskapp

    app.register_blueprint(taskapp)

    return app

    