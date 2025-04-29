WORKFLOW_REGISTRY = {}

def register_workflow(cls):
    WORKFLOW_REGISTRY[cls.__name__] = cls
    return cls

def get_registered_workflows():
    return list(WORKFLOW_REGISTRY.values())