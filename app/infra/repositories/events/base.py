from abc import ABC, abstractmethod

from app.application.registration.filters import GetEventsFilter
from app.application.registration.sorters import GetEventsSorter
from app.domain.dtos.events import EventDTO


class BaseEventRepository(ABC):
    @abstractmethod
    async def save(self, event: EventDTO): ...

    @abstractmethod
    async def delete(self, event: EventDTO): ...

    @abstractmethod
    async def find_all(
        filter: GetEventsFilter, sorter: GetEventsSorter
    ) -> list[EventDTO]: ...
