from workflow_base import WorkflowBase
from schemas import TaskInput, WorkflowResult
from model_client import ask_deepseek
from function_manager import FunctionManager
class ResearchWorkflow:
    async def run(self, task: str):
        # Step 1: 搜集资料
        info = await ask_deepseek(f"请检索并总结以下任务的信息，不超过500字：{task}", use_function_calling=True)
        
        # Step 2: 基于资料，撰写总结
        report = await ask_deepseek(f"基于以下资料撰写一份详细报告：{info}", use_function_calling=False)

        # Step 3: 保存成文件
        await FunctionManager.execute_function("save_to_file", {
            "filename": f"{task}.md",
            "content": report
        })

        return "任务完成，已生成总结文件。"
