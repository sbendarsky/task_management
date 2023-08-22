from flask import Blueprint, render_template, request, redirect, url_for, current_app
from taskapp.models import Task

taskapp = Blueprint("main", __name__)

@taskapp.route("/")
def index():
    db = current_app.db  # Access the MongoDB connection from your Flask app

    all_tasks = list(db.tasks.find())  # Retrieve all tasks from the database

    return render_template("index.html", tasks=all_tasks)

@taskapp.route("/add_task", methods=["POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        task_model = Task(current_app.db)  # Create an instance of the Task model
        task_model.create_task(title, description)  # Call the method to create a task

    return redirect(url_for("main.index"))
