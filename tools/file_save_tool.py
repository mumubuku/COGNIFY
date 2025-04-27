from pathlib import Path

async def save_to_file(filename: str, content: str) -> str:
    path = Path("outputs") / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"文件已保存到: {str(path)}"