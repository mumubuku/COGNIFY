from workflow_base import WorkflowBase
from schemas import TaskInput, WorkflowResult
from model_client import ask_deepseek

class StrategyWorkflow(WorkflowBase):
    async def run(self, task: TaskInput) -> WorkflowResult:
        prompt = f"请基于以下内容，制定一个详细的商业策略方案：\n{task.task_description}"
        result = await ask_deepseek(prompt)
        return WorkflowResult(result=result)