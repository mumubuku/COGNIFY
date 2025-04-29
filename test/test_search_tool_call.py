# test/test_tool_call.py

import asyncio
import sys
import os

# 加载项目路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from function_manager import FunctionManager
from tools.search_web_tool import SearchWebTool 
async def main():
    print("🚀 开始一键测试 SearchWebTool...")

    # 定义调用参数
    arguments = {
        "query": "2024年新能源产业趋势"
    }

    # 调用工具
    try:
        result = await FunctionManager.execute_function("SearchWebTool", arguments)
        print("\n✅ 工具调用成功！部分结果如下（前500字）：")
        print(result[:500])
    except Exception as e:
        print("\n❌ 工具调用失败:")
        print(str(e))

if __name__ == "__main__":
    asyncio.run(main())
