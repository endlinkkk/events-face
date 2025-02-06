from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from punq import Container

from app.application.registration.filters import GetEventsFilter
from app.application.registration.schemas import (
    EventQueryResponseSchema,
    EventSchema,
    VisitorRequestSchema,
    VisitorResponseSchema,
)
from app.application.registration.sorters import GetEventsSorter
from app.application.schemas import ErrorSchema
from app.domain.exceptions.base import ApplicationException
from app.logic.init import init_container
from app.logic.services import EventService

router = APIRouter(tags=["Registration"])


@router.get(
    "/events-list",
    status_code=status.HTTP_200_OK,
    description="Get events from events-provider",
    responses={
        status.HTTP_200_OK: {"model": EventQueryResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def get_events(
    filter: Annotated[GetEventsFilter, Depends()],
    sorter: Annotated[GetEventsSorter, Depends()],
    container: Annotated[Container, Depends(init_container)],
) -> EventQueryResponseSchema:
    event_service: EventService = container.resolve(EventService)
    try:
        events = await event_service.get_filtered_events(filter_=filter, sorter=sorter)
    except ApplicationException as err:
        raise HTTPException(
            status_code=err.status_code,
            detail={"error": err.message},
        )
    return EventQueryResponseSchema(
        count=len(events), items=[EventSchema.from_dto(event) for event in events]
    )


@router.post(
    "/events/{event_id}/register",
    status_code=status.HTTP_201_CREATED,
    description="Register for the event via event-provider",
    responses={
        status.HTTP_201_CREATED: {"model": VisitorResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def register_visitor(
    schema: VisitorRequestSchema,
    event_id: str,
    container: Annotated[Container, Depends(init_container)],
) -> VisitorResponseSchema:
    event_service: EventService = container.resolve(EventService)
    try:
        visitor = await event_service.register_visitor(
            event_id=event_id, visitor_dto=schema.to_dto()
        )

    except ApplicationException as err:
        raise HTTPException(
            status_code=err.status_code,
            detail={"error": err.message},
        )
    return VisitorResponseSchema.from_dto(visitor)
