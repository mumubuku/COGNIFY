from workflow_base import WorkflowBase
from schemas import TaskInput, WorkflowResult
from model_client import ask_deepseek

class DefaultWorkflow(WorkflowBase):
    async def run(self, task: TaskInput) -> WorkflowResult:
        prompt = f"请尽可能理解并完成以下任务（不超过500字总结）：\n{task.task_description}"
        result = await ask_deepseek(prompt)
        return WorkflowResult(result=result)