from datetime import datetime

from pydantic import BaseModel, EmailStr

from app.application.schemas import BaseQueryResponseSchema
from app.dtos.events import EventDTO, VisitorDTO


class EventSchema(BaseModel):
    id: str
    name: str
    event_time: datetime
    registration_deadline: datetime
    status: str
    max_visitors: int
    number_of_visitors: int

    @classmethod
    def from_dto(cls, event: EventDTO) -> "EventSchema":
        return cls(
            id=event.id,
            name=event.name,
            event_time=event.event_time,
            registration_deadline=event.registration_deadline,
            status=event.status,
            max_visitors=event.max_visitors,
            number_of_visitors=event.number_of_visitors,
        )


class EventQueryResponseSchema(BaseQueryResponseSchema[list[EventSchema]]): ...


class VisitorRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

    def to_dto(self) -> VisitorDTO:
        return VisitorDTO(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )


class VisitorResponseSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str

    @classmethod
    def from_dto(cls, visitor: VisitorDTO) -> "VisitorResponseSchema":
        return cls(
            id=visitor.id,
            first_name=visitor.first_name,
            last_name=visitor.last_name,
            email=visitor.email,
        )
