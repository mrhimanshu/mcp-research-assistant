import asyncio
from fastmcp import Client, FastMCP

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        if client.is_connected:
            print("Connected to MCP Server")

        # List available operations
        tools = await client.list_tools()
        print("\n-- Available Tools --")
        for t in tools:
            print(f"{t.name}: {t.description}")

        # Execute operations
        result = await client.call_tool("add", {"a": 5, "b": 6})
        print(f"Result {result}")
                  
if __name__ == "__main__":
    asyncio.run(main())