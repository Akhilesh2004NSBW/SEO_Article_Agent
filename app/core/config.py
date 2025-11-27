from pydantic import BaseSettings

class Settings(BaseSettings):
    serp_api_key: str | None = None
    serp_provider: str = "mock"

    class Config:
        env_file = ".env"

settings = Settings()