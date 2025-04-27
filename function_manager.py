from typing import List, Dict, Any

class FunctionManager:
    @staticmethod
    def get_registered_functions() -> List[Dict[str, Any]]:
        return [
            {
                "type": "function",
                "function": {
                    "name": "search_web",
                    "description": "在互联网上检索相关信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "需要搜索的关键词"}
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "save_to_file",
                    "description": "保存内容到本地文件",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "filename": {"type": "string", "description": "文件名"},
                            "content": {"type": "string", "description": "要保存的内容"}
                        },
                        "required": ["filename", "content"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "run_command",
                    "description": "在受控环境下执行简单命令行指令",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "command": {"type": "string", "description": "要执行的命令"}
                        },
                        "required": ["command"]
                    }
                }
            }
        ]

    @staticmethod
    async def execute_function(name: str, arguments: Dict[str, Any]) -> str:
        if name == "search_web":
            from tools.browser_search_tool import search_web
            return await search_web(arguments["query"])
        elif name == "save_to_file":
            from tools.file_save_tool import save_to_file
            return await save_to_file(arguments["filename"], arguments["content"])
        elif name == "run_command":
            from tools.shell_exec_tool import run_command
            return await run_command(arguments["command"])
        else:
            return "未知的函数调用"