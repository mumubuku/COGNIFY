from pydantic import BaseModel
from typing import Optional

class TaskInput(BaseModel):
    task_description: str

class TaskType(BaseModel):
    type: str

class WorkflowResult(BaseModel):
    result: str