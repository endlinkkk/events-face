from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventDTO:
    id: str
    name: str
    event_time: datetime
    registration_deadline: datetime
    status: str
    max_visitors: int
    number_of_visitors: int


@dataclass
class VisitorDTO:
    first_name: str
    last_name: str
    email: str
    id: str = None
