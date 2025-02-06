from app.application.registration.filters import GetEventsFilter
from app.application.registration.sorters import GetEventsSorter
from app.domain.dtos.events import EventDTO, VisitorDTO
from app.infra.caches.events.redis import RedisEventCache
from app.infra.providers.events_provider import EventProviderClient


class EventService:
    def __init__(
        self,
        events_providers_client: EventProviderClient,
        events_cache_client: RedisEventCache,
    ):
        self.events_providers_client = events_providers_client
        self.events_cache_client = events_cache_client

    async def get_filtered_events(
        self, filter_: GetEventsFilter, sorter: GetEventsSorter
    ) -> list[EventDTO]:
        events = await self.events_cache_client.get_events()
        if not events:
            events = await self.events_providers_client.fetch_events()
            for event in events:
                await self.events_cache_client.add_event(event)

        return events

    async def register_visitor(
        self, event_id: str, visitor_dto: VisitorDTO
    ) -> VisitorDTO:
        return self.events_providers_client.register_visitor(
            event_id=event_id, visitor_dto=visitor_dto
        )
