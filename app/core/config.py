from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    access_token_expire_weeks: int = 4

    model_config = SettingsConfigDict(
        env_prefix='FASTAPI_BOOKS_',
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
