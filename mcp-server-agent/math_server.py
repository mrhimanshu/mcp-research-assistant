from fastmcp import FastMCP

mcp = FastMCP("Math Server")

@mcp.tool
def add(a: int, b: int) -> int:
    "Add two number"
    return a+b

@mcp.tool
def substract(a: int, b: int) -> int:
    "Substract two number"
    return a-b

@mcp.tool
def multiply(a: int, b: int) -> int:
    "Multiply two number"
    return a+b

if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8002)