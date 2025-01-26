from dataclasses import asdict

import httpx

from app.dtos.events import EventDTO, VisitorDTO
from app.exceptions.events import (
    EventListRequestException,
    EventRegisterRequestException,
)
from app.logic.converters import convert_event_response_to_event_dto
from app.settings.config import settings


class EventWebService:
    async def get_events_list(self) -> list[EventDTO]:
        async with httpx.AsyncClient() as client:
            response = await client.get(settings.get_events_uri)

        if not response.is_success:
            raise EventListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )
        return [
            convert_event_response_to_event_dto(event_data)
            for event_data in response.json()
        ]

    async def register_event(
        self, event_id: str, visitor_dto: VisitorDTO
    ) -> VisitorDTO:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                settings.register_events_uri(event_id), json=asdict(visitor_dto)
            )

        if not response.is_success:
            raise EventRegisterRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )
        visitor_dto.id = response.json()["visitor_id"]
        return visitor_dto
