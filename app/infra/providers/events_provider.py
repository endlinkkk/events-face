from dataclasses import asdict

import httpx

from app.domain.dtos.events import EventDTO, VisitorDTO
from app.domain.exceptions.events import (
    EventListRequestException,
    EventRegisterRequestException,
)
from app.logic.converters import convert_event_response_to_event_dto


class EventProviderClient:
    """Клиент для интеграции с events-provider"""

    def __init__(self, get_events_uri: str):
        self.get_events_uri = get_events_uri

    async def fetch_events(self) -> list[EventDTO]:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.get_events_uri)

        if not response.is_success:
            raise EventListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )
        return [
            convert_event_response_to_event_dto(event_data)
            for event_data in response.json()
        ]

    async def register_visitor(
        self, event_id: str, visitor_dto: VisitorDTO
    ) -> VisitorDTO:
        async with httpx.AsyncClient() as client:
            uri = f"{self.get_events_uri}{event_id}/register/"
            response = await client.post(url=uri, json=asdict(visitor_dto))

        if not response.is_success:
            raise EventRegisterRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )
        visitor_dto.id = response.json()["visitor_id"]
        return visitor_dto
