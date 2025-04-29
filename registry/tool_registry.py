TOOL_REGISTRY = {}

def register_tool(cls):
    TOOL_REGISTRY[cls.__name__] = cls
    return cls

def get_registered_tools():
    return list(TOOL_REGISTRY.values())