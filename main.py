import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager

from database.connection import Settings
from routes.user import user_router
from routes.event import event_router

app = FastAPI()

settings = Settings()

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")

@app.get("/db-status")
async def db_status():
    try:
        # Tester une simple requête
        events = await Event.find_all().to_list()
        return {"status": "connected", "events_count": len(events)}
    except Exception as e:
        return {"status": "error", "message": str(e)}


async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)