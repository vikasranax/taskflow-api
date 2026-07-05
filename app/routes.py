from fastapi import APIRouter
from app.models import Task

router = APIRouter()
tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task

@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated: Task):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            updated.id = task_id
            tasks[i] = updated
            return updated
    return {"error": "Task not found"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}