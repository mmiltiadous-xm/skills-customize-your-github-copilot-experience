from typing import Dict

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

# In-memory store for beginner-friendly practice.
tasks: Dict[int, dict] = {}
next_id = 1


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    priority: int = Field(ge=1, le=5)


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global next_id
    created = {"id": next_id, **task.model_dump()}
    tasks[next_id] = created
    next_id += 1
    return created


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
