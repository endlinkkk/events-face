from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    EVENTS_PROVIDER_ADDR: str

    REDIS_PASSWORD: str
    REDIS_USER: str
    REDIS_USER_PASSWORD: str
    REDIS_PORT: int
    REDIS_HOST: str

    @property
    def get_events_uri(self) -> str:
        return self.EVENTS_PROVIDER_ADDR
