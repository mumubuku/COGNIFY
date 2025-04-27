# ========== model_client.py ==========
import os
import httpx
import json
from dotenv import load_dotenv
from function_manager import FunctionManager
from pathlib import Path
import uuid

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

async def ask_deepseek(prompt: str, use_function_calling: bool = False) -> str:
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    messages = [
        {"role": "system", "content": "你是DeepSeek智能助手。"},
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": "deepseek-r1-250120",
        "messages": messages,
        "temperature": 0.3
    }

    if use_function_calling:
        payload["tools"] = FunctionManager.get_registered_functions()
        payload["tool_choice"] = "auto"

    conversation_log = []

    async with httpx.AsyncClient(timeout=60.0) as client:
        while True:
            payload["messages"] = messages
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            choice = data["choices"][0]["message"]
            content = choice.get("content", "").strip()

            # 保存用户提问到日志（如果是第一次）
            if len(conversation_log) == 0:
                conversation_log.append({"user_message": prompt})

            # 保存助手返回到日志
            conversation_log.append({"assistant_message": choice})

            if "tool_calls" in choice:
                for tool_call in choice["tool_calls"]:
                    func_name = tool_call["function"]["name"]
                    func_args = tool_call["function"]["arguments"]

                    parsed_args = json.loads(func_args) if isinstance(func_args, str) else func_args
                    result = await FunctionManager.execute_function(func_name, parsed_args)

                    tool_call_id = tool_call.get("id", str(uuid.uuid4()))

                    messages.append({
                        "role": "assistant",
                        "tool_calls": [tool_call]
                    })
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call_id,
                        "name": func_name,
                        "content": result
                    })

                    # 保存工具调用请求到日志
                    conversation_log.append({
                        "tool_call": {
                            "function_name": func_name,
                            "arguments": parsed_args
                        }
                    })
                    # 保存工具执行结果到日志
                    conversation_log.append({
                        "tool_result": {
                            "function_name": func_name,
                            "result": result
                        }
                    })
                continue
            else:
                # 会话结束，保存完整对话日志
                save_conversation_log(conversation_log)
                return content or "(无内容输出)"


def save_conversation_log(log_data: list):
    path = Path("outputs/conversation_logs")
    path.mkdir(parents=True, exist_ok=True)
    log_file = path / f"conversation_{uuid.uuid4()}.jsonl"
    with log_file.open("w", encoding="utf-8") as f:
        for entry in log_data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
