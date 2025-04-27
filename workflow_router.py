from task_classifier import classify_task
from workflows.research_workflow import ResearchWorkflow
from workflows.writing_workflow import WritingWorkflow
from workflows.strategy_workflow import StrategyWorkflow
from workflows.default_workflow import DefaultWorkflow

async def route_task(task):
    task_type = classify_task(task)
    if task_type.type == "research":
        return await ResearchWorkflow().run(task)
    elif task_type.type == "writing":
        return await WritingWorkflow().run(task)
    elif task_type.type == "strategy":
        return await StrategyWorkflow().run(task)
    else:
        return await DefaultWorkflow().run(task)