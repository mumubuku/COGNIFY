from registry.tool_registry import register_tool
import httpx
from urllib.parse import quote, unquote, urlparse, parse_qs
from selectolax.parser import HTMLParser

@register_tool
class SearchWebTool:
    @staticmethod
    def get_tool_schema():
        return {
            "name": "SearchWebTool",
            "description": "通过DuckDuckGo搜索检索关键词信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "需要检索的关键词，比如 '2024年新能源产业趋势'"
                    }
                },
                "required": ["query"]
            }
        }

    async def run(self, arguments: dict) -> str:
        query = arguments["query"]
        query_encoded = quote(query)

        url = f"https://duckduckgo.com/html/?q={query_encoded}"

        print(f"🦆 使用DuckDuckGo检索: {query}")

        try:
            async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
                response = await client.get(url)
                response.raise_for_status()

                html = response.text
                parser = HTMLParser(html)

                results = []
                for a_tag in parser.css('a.result__a')[:5]:  # 抓前5条搜索结果
                    title = a_tag.text(strip=True)
                    link = a_tag.attributes.get('href', '')

                    # 处理 duckduckgo 跳转链接
                    if link.startswith('//duckduckgo.com/l/?uddg='):
                        parsed_link = urlparse("https:" + link)
                        query_params = parse_qs(parsed_link.query)
                        real_link = unquote(query_params.get('uddg', [''])[0])
                    else:
                        real_link = link

                    results.append(f"【{title}】\n🔗 {real_link}")

                return "\n\n".join(results) if results else "未找到相关信息。"

        except Exception as e:
            print(f"❌ DuckDuckGo搜索失败: {e}")
            return f"搜索失败: {e}"
