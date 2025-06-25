from anthropic import Anthropic
from src.agents.tools import get_tools
from src.settings import CONF
from src.agents.tool_logic import (
    get_weather, get_news, get_exchange_rate,
    get_joke, get_stock_price, get_quote, send_email
)

class MCPHandler:
    """
    Handles the MCP pipeline: sends the user message to Claude,
    executes requested tools, and returns the final output.
    """

    def __init__(self):
        self.client = Anthropic(api_key=CONF.anthropic_api_key)
        self.tools = get_tools()
        self.tool_map = {
            "get_weather": get_weather,
            "get_news": get_news,
            "get_exchange_rate": get_exchange_rate,
            "get_joke": get_joke,
            "get_stock_price": get_stock_price,
            "get_quote": get_quote,
            "send_email": send_email
        }

    async def run(self, user_message: str):
        messages = [{"role": "user", "content": user_message}]
        while True:
            response = self.client.beta.tools.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                system="You are a helpful assistant with access to several tools. Use them as needed.",
                tools=self.tools,
                messages=messages
            )

            last = response.content[0]
            if last.type == "tool_use":
                tool_name = last.name
                tool_input = last.input
                func = self.tool_map[tool_name]

                # Run tool function and get result
                result = await func(**tool_input)

                # Append result to conversation
                messages.append({
                    "role": "tool",
                    "tool_name": tool_name,
                    "content": result
                })
            else:
                return {"reply": last.text}
