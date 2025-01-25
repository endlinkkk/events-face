from fastapi import status
from fastapi.routing import APIRouter

from app.application.registration.schemas import EventQueryResponseSchema, VisitorSchema
from app.application.schemas import ErrorSchema

router = APIRouter(tags=["Registration"])


@router.get(
    "/events",
    status_code=status.HTTP_200_OK,
    description="Get events from events-provider",
    responses={
        status.HTTP_200_OK: {"model": EventQueryResponseSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def get_events() -> EventQueryResponseSchema: ...


@router.post(
    "/events/{event_id}/register",
    status_code=status.HTTP_201_CREATED,
    description="Register for the event via event-provider",
    responses={
        status.HTTP_201_CREATED: {"model": VisitorSchema},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def register_event(event_id: str) -> VisitorSchema: ...
