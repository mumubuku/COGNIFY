from abc import ABC, abstractmethod
from schemas import TaskInput, WorkflowResult

class WorkflowBase(ABC):
    @abstractmethod
    async def run(self, task: TaskInput) -> WorkflowResult:
        pass