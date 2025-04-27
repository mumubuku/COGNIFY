from workflow_base import WorkflowBase
from schemas import TaskInput, WorkflowResult
from model_client import ask_deepseek

class WritingWorkflow(WorkflowBase):
    async def run(self, task: TaskInput) -> WorkflowResult:
        prompt = f"请基于以下主题，撰写一篇条理清晰的小短文：\n{task.task_description}"
        result = await ask_deepseek(prompt)
        return WorkflowResult(result=result)
