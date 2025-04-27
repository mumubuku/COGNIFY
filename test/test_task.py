import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asyncio
from schemas import TaskInput
from workflows.research_workflow import ResearchWorkflow

async def main():
    workflow = ResearchWorkflow()
    task = TaskInput(task_description="评价孙中山，保存到本地")
    result = await workflow.run(task)
    print("\n--- 任务输出 ---\n")
    print(result.result)

if __name__ == "__main__":
    asyncio.run(main())
