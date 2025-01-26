from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter

from app.application.registration.schemas import (
    EventQueryResponseSchema,
    EventSchema,
    VisitorRequestSchema,
    VisitorResponseSchema,
)
from app.application.schemas import ErrorSchema
from app.exceptions.base import ApplicationException
from app.logic.services import EventWebService

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
    event_service: Annotated[EventWebService, Depends(EventWebService)],
) -> EventQueryResponseSchema:
    try:
        events = await event_service.get_events_list()
        return EventQueryResponseSchema(
            count=len(events), items=[EventSchema.from_dto(event) for event in events]
        )
    except ApplicationException as err:
        raise HTTPException(
            status_code=err.status_code,
            detail={"error": err.message},
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
async def register_event(
    schema: VisitorRequestSchema,
    event_id: str,
    event_service: Annotated[EventWebService, Depends(EventWebService)],
) -> VisitorResponseSchema:
    try:
        visitor = await event_service.register_event(
            event_id=event_id, visitor_dto=schema.to_dto()
        )
        return VisitorResponseSchema.from_dto(visitor)
    except ApplicationException as err:
        raise HTTPException(
            status_code=err.status_code,
            detail={"error": err.message},
        )
