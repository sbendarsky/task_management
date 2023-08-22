from flask import Blueprint, render_template, current_app, request, redirect, url_for

taskapp = Blueprint("main", __name__)

@taskapp.route("/")
def index():
    # Use current_app to access the app instance
    db = current_app.db

    # Now you can work with the db object
    tasks_collection = db.tasks
    all_tasks = tasks_collection.find()

    return render_template("index.html", tasks=all_tasks)

@taskapp.route("/add_task", methods=["POST"])
def add_task():
    db = current_app.db

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        
        tasks_collection = db.tasks
        tasks_collection.insert_one({"title": title, "description": description})

    return redirect(url_for("main.index"))
