import os
import asyncio
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient
from rich import print

async def main():

    # # Create MCPClient from configuration dictionary for stdio
    # client = MCPClient.from_config_file(os.path.join('mcp.json'))

    # Create MCPClient from configuration dictionary for http
    client = MCPClient.from_config_file(os.path.join('mcp-http.json'))

    # Create LLM
    llm = ChatOllama(base_url="http://localhost:11434", model="qwen3:8b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30, use_server_manager=True)

    # Run the query
    result = await agent.run(
        "What's the weather in London and the 3-day forecast?",
    )
    print(f"\nResult: {result}")

    # Run the query
    result = await agent.run(
        "What's 3 mul by 7?",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())