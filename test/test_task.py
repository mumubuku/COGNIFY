# ========== test/test_task.py ==========

import sys
import os

# 保证项目根目录在sys.path里
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

import asyncio
from workflows.research_workflow import ResearchWorkflow
from schemas.task_input import TaskInput


async def run_test_task():
    workflow = ResearchWorkflow()

    task_input = TaskInput(
        task="调研2025年美中贸易关系",
        allow_internet=True,
        priority=1,
        user_preferences={}
    )

    result = await workflow.run(task_input)

    print("\n========== 测试结果 ==========")
    print("📝 总结内容:\n", result.content)
    print("🛠 使用工具:", result.used_tools)
    print("📄 日志文件路径:", result.logs_path)
    print("✅ 状态:", result.status)
    print("================================\n")


if __name__ == "__main__":
    asyncio.run(run_test_task())
