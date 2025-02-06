from datetime import datetime

from app.domain.dtos.events import EventDTO


def convert_event_response_to_event_dto(event_data: dict) -> EventDTO:
    return EventDTO(
        id=event_data["id"],
        name=event_data["name"],
        event_time=datetime.fromisoformat(event_data["event_time"]),
        registration_deadline=datetime.fromisoformat(
            event_data["registration_deadline"]
        ),
        status=event_data["status"],
        max_visitors=event_data["max_visitors"],
        number_of_visitors=event_data["number_of_visitors"],
    )
