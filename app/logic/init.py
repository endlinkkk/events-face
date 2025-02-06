from functools import lru_cache

from punq import Container, Scope

from app.infra.caches.events.redis import RedisEventCache
from app.infra.providers.events_provider import EventProviderClient
from app.logic.services import EventService
from app.settings.config import Settings


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(Settings, instance=Settings(), scope=Scope.singleton)
    settings: Settings = container.resolve(Settings)

    def init_event_provider_client() -> EventProviderClient:
        return EventProviderClient(
            get_events_uri=settings.get_events_uri,
        )

    container.register(EventProviderClient, factory=init_event_provider_client)

    def init_redis_event_cache() -> RedisEventCache:
        return RedisEventCache(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
        )

    container.register(RedisEventCache, factory=init_redis_event_cache)

    def init_events_service() -> EventService:
        return EventService(
            events_providers_client=container.resolve(EventProviderClient),
            events_cache_client=container.resolve(RedisEventCache),
        )

    container.register(EventService, factory=init_events_service)

    return container
