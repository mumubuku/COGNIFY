from workflows.workflow_base import WorkflowBase
from schemas.task_input import TaskInput
from schemas.task_result import TaskResult
from model_client import ask_deepseek
from function_manager import FunctionManager

class ResearchWorkflow(WorkflowBase):
    async def run(self, task_input: TaskInput) -> TaskResult:
        task_desc = task_input.task

        # Step 1: 搜索资料
        search_info = await ask_deepseek(
            f"请检索并总结以下任务的信息，不超过500字：{task_desc}",
            use_function_calling=True
        )

        # Step 2: 写总结
        writing_info = await ask_deepseek(
            f"基于以下资料撰写一份详细报告：{search_info.content}",
            use_function_calling=False
        )


        # Step 4: 返回TaskResult
        return TaskResult(
            content=writing_info.content,
            used_tools=list(set((search_info.used_tools or []) + (writing_info.used_tools or []) + ["save_to_file"])),
            logs_path=writing_info.logs_path,
            status="success"
        )
