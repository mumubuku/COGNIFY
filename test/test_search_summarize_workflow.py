# test/test_search_summarize_workflow.py
import sys
import os
import asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from workflows.search_summarize_workflow import SearchSummarizeWorkflow
from schemas.task_input import TaskInput
from tools.search_web_tool import SearchWebTool
from tools.fetch_web_content_tool import FetchWebContentTool



async def main():
    workflow = SearchSummarizeWorkflow()
    task = TaskInput(task="总结中美贸易战局")
    result = await workflow.run(task)

    print("📝 总结内容：\n", result.content[:1000])
    print("🛠 使用工具：", result.used_tools)
    print("✅ 状态：", result.status)

if __name__ == "__main__":
    asyncio.run(main())
