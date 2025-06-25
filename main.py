from fastapi import FastAPI, Request
from src.agents.mcp_handler import MCPHandler

app = FastAPI()
mcp_handler = MCPHandler()

@app.post("/mcp")
async def mcp_entry(request: Request):
    """
    FastAPI endpoint that receives a user message and routes it through the MCP pipeline.
    """
    data = await request.json()
    user_message = data.get("message")
    return await mcp_handler.run(user_message)
