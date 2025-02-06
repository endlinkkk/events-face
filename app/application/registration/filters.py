from enum import Enum

from pydantic import BaseModel


class EventStatus(Enum):
    open = "open"
    registration_closed = "registration closed"
    finished = "finished"
    cancelled = "cancelled"


class GetEventsFilter(BaseModel):
    registration_deadline: bool | None = None
    name: str | None = None
    status: EventStatus | None = None
