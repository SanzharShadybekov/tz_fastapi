from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, condecimal


class BetsCreate(BaseModel):
    event_identifier: str = Field(..., description="bets event identifier",
                                  example='event-1')
    bet_amount: condecimal(gt=0, decimal_places=2, max_digits=10) = Field(
        ..., description="bets amount", example=10_000.00)


class BetsUpdate(BaseModel):
    status: Literal['won', 'lost'] = Field(..., description="status",
                                           example="won")


class BetsRead(BetsCreate):
    id: int = Field(..., description="bet id", example=1)
    status: str = Field(..., description="status", example="not_played")
    created_at: datetime = Field(..., description="time created",
                                 example="2024-01-01T00:00:00")
    updated_at: datetime = Field(..., description="time last updated",
                                 example="2024-01-01T00:00:00")

    class Config:
        from_attributes = True
