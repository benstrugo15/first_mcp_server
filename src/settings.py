from functools import lru_cache
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    anthropic_api_key: str
    news_api_key: str
    finnhub_api_key: str


@lru_cache()
def _load_settings() -> Settings:
    return Settings(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
        news_api_key=os.getenv("NEWS_API_KEY"),
        finnhub_api_key=os.getenv("FINNHUB_API_KEY")
    )


CONF = _load_settings()
