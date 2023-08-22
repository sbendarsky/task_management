from flask import Flask
from taskapp.views import taskapp
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    # MongoDB configuration
    app.config["MONGO_URI"] = "mongodb://localhost:27017/taskapp"
    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.get_database()

    app.register_blueprint(taskapp)

    return app
