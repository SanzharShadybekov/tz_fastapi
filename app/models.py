from sqlalchemy import (Column, String, Integer, DateTime,
                        DECIMAL, CheckConstraint, Enum, sql)
from core.db import Base
import enum


class BetStatus(enum.Enum):
    not_played = "ещё не сыграла"
    won = "выиграла"
    lost = "проиграла"


class Bet(Base):
    __tablename__ = 'apps_bets'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    event_identifier = Column(String(50))
    bet_amount = Column(DECIMAL(10, 2), CheckConstraint('price > 0'),
                        nullable=False)
    status = Column(Enum(BetStatus), default=BetStatus.not_played.name,)
    created_at = Column(DateTime(timezone=True), default=sql.func.now())
    updated_at = Column(DateTime(timezone=True), default=sql.func.now(),
                        onupdate=sql.func.now())
