# tools/fetch_web_content_tool.py
from registry.tool_registry import register_tool
import httpx
from readability import Document
from selectolax.parser import HTMLParser

@register_tool
class FetchWebContentTool:
    @staticmethod
    def get_tool_schema():
        return {
            "name": "FetchWebContentTool",
            "description": "抓取网页正文内容（自动提取，兼容大部分新闻、博客网站）",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "需要抓取正文内容的网页URL"
                    }
                },
                "required": ["url"]
            }
        }

    async def run(self, arguments: dict) -> str:
        url = arguments["url"]
        print(f"🌐 抓取网页内容: {url}")

        try:
            async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
                response = await client.get(url)
                response.raise_for_status()

                html = response.text

                # 使用 readability 优先提取正文
                doc = Document(html)
                content_html = doc.summary()
                parser = HTMLParser(content_html)

                # 进一步提取干净的文字段落
                paragraphs = []
                for p_tag in parser.css('p'):
                    text = p_tag.text(strip=True)
                    if len(text) > 30:
                        paragraphs.append(text)

                content = "\n\n".join(paragraphs)
                if not content:
                    return "未能提取有效正文，请检查网页是否为动态渲染。"
                
                return content[:5000]  # 限制最大返回长度
        except Exception as e:
            print(f"❌ 抓取失败: {e}")
            return f"抓取失败: {e}"
