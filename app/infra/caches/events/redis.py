from dataclasses import asdict
from datetime import datetime, timezone

import redis

from app.domain.dtos.events import EventDTO
from app.infra.caches.events.base import BaseEventCache
from app.logic.converters import convert_event_response_to_event_dto


class RedisEventCache(BaseEventCache):
    def __init__(self, host: str, port: int, password: str):
        self.redis_client = redis.Redis(host=host, port=port, password=password)

    async def add_event(self, event: EventDTO):
        event_data = asdict(event)
        for key, value in event_data.items():
            if isinstance(value, datetime):
                event_data[key] = value.isoformat()

        key = f"event:{event.id}"
        self.redis_client.hset(key, mapping=event_data)

        expire_time = int(
            (event.event_time - datetime.now(timezone.utc)).total_seconds()
            + 7 * 24 * 60 * 60
        )
        self.redis_client.expire(key, expire_time)

    async def get_events(self) -> list[EventDTO]:
        events = []
        keys = self.redis_client.scan_iter("event:*")
        for key in keys:
            event_data = self.redis_client.hgetall(key)
            decoded_event_data = {
                k.decode("utf-8"): v.decode("utf-8") for k, v in event_data.items()
            }
            events.append(decoded_event_data)
        return [
            convert_event_response_to_event_dto(event_data=event) for event in events
        ]
