# test/test_fetch_web_content_tool.py
import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.fetch_web_content_tool import FetchWebContentTool

async def test_fetch_web_content():
    tool = FetchWebContentTool()
    
    # 这里可以换成任何公开的新闻或者文章网页
    test_url = "https://m.163.com/news/article/JU7V0J9V000189FH.html"  # 例如BBC的一篇新闻
    arguments = {"url": test_url}

    print(f"🚀 测试抓取网页正文内容: {test_url}")
    result = await tool.run(arguments)

    print("\n✅ 抓取成功！部分正文内容如下（前500字）：\n")
    print(result[:500])

if __name__ == "__main__":
    asyncio.run(test_fetch_web_content())
