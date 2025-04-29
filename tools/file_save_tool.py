from pathlib import Path
from registry.tool_registry import register_tool

@register_tool
class SaveToFileTool:
    @staticmethod
    def get_tool_schema():
        return {
            "name": "SaveToFileTool",
            "description": "保存文本内容到本地文件",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "要保存的文件名，例如report.md"
                    },
                    "content": {
                        "type": "string",
                        "description": "要保存的文本内容"
                    }
                },
                "required": ["filename", "content"]
            }
        }

    async def run(self, arguments: dict) -> str:
        filename = arguments["filename"]
        content = arguments["content"]

        path = Path("outputs") / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"文件已保存到: {str(path)}"
