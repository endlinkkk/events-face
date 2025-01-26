from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    EVENTS_PROVIDER_ADDR: str

    @property
    def get_events_uri(self) -> str:
        return self.EVENTS_PROVIDER_ADDR

    def register_events_uri(self, event_id: str) -> str:
        return f"{self.EVENTS_PROVIDER_ADDR}{event_id}/register/"


settings = Settings()
