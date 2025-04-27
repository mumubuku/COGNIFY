from fastapi import FastAPI
from schemas import TaskInput, WorkflowResult
from workflow_router import route_task

app = FastAPI()

@app.post("/task", response_model=WorkflowResult)
async def process_task(task: TaskInput):
    result = await route_task(task)
    return result
