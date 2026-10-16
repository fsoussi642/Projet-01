from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI(title="Task Service",version="1.0.0",description="Microservice exemple pour CI/CD")
class Task(BaseModel):
    """Modèle d'entrée validé automatiquement par Pydantic."""
    title:str=Field(min_length=1,max_length=120)
    completed:bool=False
_tasks:dict[int,Task]={}; _next_id=1

@app.get("/health")
def health():
    """Endpoint de santé consommé par le healthcheck du conteneur."""
    return {"status":"ok","service":"task-service"}

@app.get("/tasks")
def list_tasks():
    return [{"id":i,**task.model_dump()} for i,task in _tasks.items()]

@app.post("/tasks",status_code=201)
def create_task(task:Task):
    global _next_id
    task_id=_next_id; _next_id+=1; _tasks[task_id]=task
    return {"id":task_id,**task.model_dump()}
