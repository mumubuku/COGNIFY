from schemas import TaskInput, TaskType

def classify_task(task: TaskInput) -> TaskType:
    desc = task.task_description.lower()
    if any(kw in desc for kw in ["研究", "分析", "趋势"]):
        return TaskType(type="research")
    elif any(kw in desc for kw in ["写作", "文章", "总结"]):
        return TaskType(type="writing")
    elif any(kw in desc for kw in ["策略", "计划", "商业"]):
        return TaskType(type="strategy")
    else:
        return TaskType(type="default")