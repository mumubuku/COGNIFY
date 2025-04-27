import httpx

async def search_web(query: str) -> str:
    url = f"https://www.baidu.com/s?wd={query}"
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text[:2000]
    except httpx.RequestError as e:
        return f"检索时发生错误: {e}"
