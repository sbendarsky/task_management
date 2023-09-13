from sqlalchemy.orm import Session
from models import Task
from schemas import TaskSchema

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """Get a list of tasks with optional pagination."""
    return db.query(Task).offset(skip).limit(limit).all()

def get_task_by_id(db: Session, task_id: int):
    """Get a task by its ID."""
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskSchema):
    """Create a new task and return it."""
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    """Delete a task by its ID."""
    db_task = get_task_by_id(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()

def update_task(db: Session, task_id: int, task: TaskSchema):
    """Update a task's information and return the updated task."""
    db_task = get_task_by_id(db, task_id)
    if db_task:
        for field, value in task.dict().items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
        return db_task
