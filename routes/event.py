from beanie import PydanticObjectId
from fastapi import APIRouter, Body, HTTPException, status
from database.connection import Database
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


from models.event import Event, EventUpdate
from typing import List

event_database = Database(Event)
event_router = APIRouter(
    tags=["Events"]
)

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event

@event_router.post("/new")
async def create_event(body:Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully"
    }

@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate = Body(...)) -> Event:
    try:
        updated_event = await event_database.update(id, body)
        if not updated_event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event with supplied ID does not exist"
            )
        return updated_event
    except Exception as e:
        logging.error(f"Error updating event: {e!r}")
        logging.error(f"Error type: {type(e)}")
        raise

@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully"
    }
