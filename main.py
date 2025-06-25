from fastapi import FastAPI
from pydantic import BaseModel
from src.agents.mcp_runtime import mcp

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/mcp")
async def run_mcp(query: Query):
    response = await mcp.run(query.message)
    return {"response": response}
