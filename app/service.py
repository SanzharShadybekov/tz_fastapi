from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from .models import Bet
from .schemas import BetsCreate, BetsRead, BetsUpdate


async def get_bets_list(session: AsyncSession):
    result = await session.execute(select(Bet))
    bets = result.scalars().all()
    return [BetsRead.from_orm(bet) for bet in bets]


async def create_bets(bet: BetsCreate, session: AsyncSession):
    bet = Bet(**bet.dict())
    session.add(bet)
    await session.commit()
    await session.refresh(bet)
    return bet


async def update_bets(event_id: str, status_update: BetsUpdate,
                      session: AsyncSession):
    updated_bets = []
    async with session.begin():
        result = await session.execute(select(Bet).filter(
            Bet.event_identifier == event_id))
        bets = result.scalars().all()

        if not bets:
            raise HTTPException(status_code=404, detail="event not found")

        for bet in bets:
            bet.status = status_update.status
            updated_bets.append(BetsRead.from_orm(bet))

        await session.commit()
    return updated_bets
