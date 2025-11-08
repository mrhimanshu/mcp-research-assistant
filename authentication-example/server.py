from fastapi import FastAPI
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider
from fastmcp.server.dependencies import get_access_token
from dotenv import load_dotenv
import os

load_dotenv("../.env", override=True)

# The GitHubProvider handles GitHub's token format and validation
auth_provider = GitHubProvider(
    client_id=os.getenv("CLIENT_ID"),  # Your GitHub OAuth App Client ID # type: ignore
    client_secret=os.getenv("CLIENT_SECRET"),     # Your GitHub OAuth App Client Secret # type: ignore
    base_url="http://localhost:8000",   # Must match your OAuth App configuration
    redirect_path="sum/auth/callback"   # Default value, customize if needed
)

mcp = FastMCP("Demo", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated GitHub user."""
    token = get_access_token()
    # The GitHubProvider stores user data in token claims
    return {
        "github_user": token.claims.get("login"), # type: ignore
        "name": token.claims.get("name"), # type: ignore
        "email": token.claims.get("email") # type: ignore
    }

@mcp.tool
def add(a: int, b: int) -> int:
    "Add two number"
    return a+b

# Create ASGI app from MCP server
mcp_app = mcp.http_app(path="/mcp")

app = FastAPI(title="Sum", lifespan=mcp_app.lifespan)

app.mount("/", mcp_app)

if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)