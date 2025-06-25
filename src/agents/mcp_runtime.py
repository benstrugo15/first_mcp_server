from fastmcp import FastMCP
from src.agents.tool_logic import (
    get_weather, get_news, get_exchange_rate,
    get_joke, get_stock_price, get_quote, send_email
)

mcp = FastMCP(name="ClaudeMCP")

@mcp.tool()
async def get_weather(city: str) -> str:
    return await get_weather(city)

@mcp.tool()
async def get_news(country: str) -> str:
    return await get_news(country)

@mcp.tool()
async def get_exchange_rate(from_currency: str, to_currency: str) -> str:
    return await get_exchange_rate(from_currency, to_currency)

@mcp.tool()
async def get_joke() -> str:
    return await get_joke()

@mcp.tool()
async def get_stock_price(symbol: str) -> str:
    return await get_stock_price(symbol)

@mcp.tool()
async def get_quote() -> str:
    return await get_quote()

@mcp.tool()
async def send_email(to: str, subject: str, body: str) -> str:
    return await send_email(to, subject, body)

if __name__ == "__main__":
    mcp.run()
