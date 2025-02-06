from datetime import datetime

from pydantic import BaseModel


class GetEventsSorter(BaseModel):
    events_time: datetime | None = None
