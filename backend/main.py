from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.item import *

app = FastAPI()


# Set Endpoints

@app.get(f"/api/get_calendar_data")
async def get_calendar_data(time_payload: CalendarData, session: AsyncSession)
