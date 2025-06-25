from typing import List, Dict

def get_tools() -> List[Dict]:
    """
    Returns a list of tools available for Claude to use via the MCP interface.
    Each tool includes a name, description, and input schema following JSON Schema format.
    """
    return [
        {
            "name": "get_weather",
            "description": "Retrieves weather information for a given city.",
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"]
            }
        },
        {
            "name": "get_news",
            "description": "Fetches the latest news headlines for a specific country.",
            "input_schema": {
                "type": "object",
                "properties": {"country": {"type": "string"}},
                "required": ["country"]
            }
        },
        {
            "name": "get_exchange_rate",
            "description": "Returns exchange rate between two currencies.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "from_currency": {"type": "string"},
                    "to_currency": {"type": "string"}
                },
                "required": ["from_currency", "to_currency"]
            }
        },
        {
            "name": "get_joke",
            "description": "Returns a random joke.",
            "input_schema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "get_stock_price",
            "description": "Fetches the current price of a given stock symbol.",
            "input_schema": {
                "type": "object",
                "properties": {"symbol": {"type": "string"}},
                "required": ["symbol"]
            }
        },
        {
            "name": "get_quote",
            "description": "Returns an inspirational quote.",
            "input_schema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "send_email",
            "description": "Sends an email with a subject and body to the given address.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "to": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["to", "subject", "body"]
            }
        }
    ]
