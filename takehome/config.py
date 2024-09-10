from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

# ============================ Team Matcher Server ============================

# You may modify this file as needed. All environment variables should be set here.

# =============================================================================


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Secret key for optional JWT authentication challenge
    SECRET_KEY: str


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
