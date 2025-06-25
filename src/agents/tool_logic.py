from src.settings import CONF
import httpx

async def get_weather(city: str) -> str:
    print("Getting weather")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://wttr.in/" + city + "?format=3")
        return r.text.strip()

async def get_news(country: str) -> str:
    print("Getting news")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://newsapi.org/v2/top-headlines", params={
            "country": country,
            "apiKey": CONF.news_api_key
        })
        articles = r.json().get("articles", [])[:3]
        return "\n".join([f"- {a['title']}" for a in articles]) or "No news found."

async def get_exchange_rate(from_currency: str, to_currency: str) -> str:
    print("Getting exchange rate")
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://api.exchangerate.host/convert", params={
            "from": from_currency,
            "to": to_currency
        })
        data = r.json()
        rate = data.get("result")
        return f"1 {from_currency} = {rate} {to_currency}" if rate else "Rate not found."

async def get_joke() -> str:
    print("Getting joke")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://official-joke-api.appspot.com/random_joke")
        data = r.json()
        return f"{data['setup']} - {data['punchline']}"

async def get_stock_price(symbol: str) -> str:
    print("getting stock price")
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://finnhub.io/api/v1/quote", params={
            "symbol": symbol,
            "token": CONF.finnhub_api_key
        })
        data = r.json()
        return f"{symbol.upper()} current price: ${data.get('c', 'N/A')}"

async def get_quote() -> str:
    print("Getting quote")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://api.quotable.io/random")
        data = r.json()
        return f"{data['content']} — {data['author']}"

async def send_email(to: str, subject: str, body: str) -> str:
    # Placeholder: integrate with a real email service (e.g., SendGrid/Mailgun)
    print(f"Sending email to {to} with subject '{subject}' and body: {body}")
    return f"Email sent to {to}."
