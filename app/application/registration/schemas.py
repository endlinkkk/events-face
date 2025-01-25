from datetime import datetime

from pydantic import BaseModel

from app.application.schemas import BaseQueryResponseSchema


class EventSchema(BaseModel):
    id: str
    name: str
    event_time: datetime
    registration_deadline: datetime
    status: str
    max_visitors: int
    number_of_visitors: int


class EventQueryResponseSchema(BaseQueryResponseSchema[list[EventSchema]]): ...


class VisitorSchema(BaseModel):
    id: str
