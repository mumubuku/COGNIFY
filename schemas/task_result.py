from typing import List, Optional
from pydantic import BaseModel

class TaskResult(BaseModel):
    content: str  # 最终生成内容
    used_tools: Optional[List[str]] = []
    logs_path: Optional[str] = None
    status: str = "success"  # success / failure
    error_message: Optional[str] = None