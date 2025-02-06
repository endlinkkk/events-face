from abc import ABC, abstractmethod

from app.domain.dtos.events import EventDTO


class BaseEventCache(ABC):
    @abstractmethod
    async def add_event(self, event: EventDTO): ...

    @abstractmethod
    async def get_events(self) -> list[EventDTO]: ...
