import asyncio

ALLOWED_COMMANDS = ["ls", "pwd", "whoami"]

async def run_command(command: str) -> str:
    if any(command.startswith(allowed) for allowed in ALLOWED_COMMANDS):
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if stderr:
            return f"错误: {stderr.decode()}"
        return stdout.decode()
    else:
        return "禁止执行该命令"
