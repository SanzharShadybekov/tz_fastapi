from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import BetsRead, BetsCreate, BetsUpdate
from app.service import get_bets_list, create_bets, update_bets
from core.db import get_session

app = FastAPI()


@app.get("/bets/", response_model=List[BetsRead], tags=['bets'])
async def bets_list(session: AsyncSession = Depends(get_session)):
    return await get_bets_list(session=session)


@app.post("/bets/", response_model=BetsRead, tags=['bets'])
async def bets_create(bet: BetsCreate,
                      session: AsyncSession = Depends(get_session)):
    return await create_bets(bet=bet, session=session)


@app.put("/events/{event_id}/", response_model=List[BetsRead], tags=['events'])
async def update_event_status(event_id: str, status_update: BetsUpdate,
                              session: AsyncSession = Depends(get_session)):
    return await update_bets(event_id=event_id, status_update=status_update,
                             session=session)
