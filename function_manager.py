from registry.tool_registry import get_registered_tools

class FunctionManager:
    @staticmethod
    def get_registered_functions():
        tools = []
        for tool_cls in get_registered_tools():
            tools.append(tool_cls.get_tool_schema())  # 每个Tool类提供自己的schema
        return tools

    @staticmethod
    async def execute_function(function_name: str, arguments: dict):
        for tool_cls in get_registered_tools():
            if tool_cls.__name__ == function_name:
                return await tool_cls().run(arguments)
        raise ValueError(f"Function {function_name} not found.")