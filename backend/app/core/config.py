from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "SecureEscrow AI"
    # Provide a default for local dev if not set
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    GEMINI_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
