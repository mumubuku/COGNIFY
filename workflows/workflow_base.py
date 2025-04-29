from abc import ABC, abstractmethod
from schemas.task_input import TaskInput
from schemas.task_result import TaskResult

class WorkflowBase(ABC):
    @abstractmethod
    async def run(self, task: TaskInput) -> TaskResult:
        pass