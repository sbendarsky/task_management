from pymongo import MongoClient

class Task:
    def __init__(self, db):
        self.db = db

    def create_task(self, title, description):
        task = {
            "title": title,
            "description": description
        }
        self.db.tasks.insert_one(task)
