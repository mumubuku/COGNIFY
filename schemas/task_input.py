from pydantic import BaseModel
from typing import Dict

class TaskInput(BaseModel):
    task: str  # 任务描述，核心
    allow_internet: bool = True  # 是否允许联网，默认允许
    priority: int = 1  # 优先级（预留）
    user_preferences: Dict = {}  # 预留未来个性化配置