import asyncio
from aioengine import GoogleEngine, EngineError

async def main():
    api_key = "ABCDEFGHIJKLMNOP"
    cse_id = "1234567890"
    
    async with GoogleEngine(api_key, cse_id) as engine:
        try:
            query = "python"
            results = await engine.search(query, num=5)
            for result in results:
                print(result.link)

        except EngineError as error:
            error.display_error()

if __name__ == "__main__":
    asyncio.run(main())