from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, condecimal


class BetsCreate(BaseModel):
    event_identifier: str = Field(..., description='bets event identifier',
                                  json_schema_extra={'example': 'event-1'})
    bet_amount: condecimal(gt=0, decimal_places=2, max_digits=10) = Field(
        ..., description='bets amount', json_schema_extra={'example': 10_000.00})


class BetsUpdate(BaseModel):
    status: Literal['won', 'lost'] = Field(..., description='status',
                                           json_schema_extra={'example': 'won'})


class BetsRead(BetsCreate):
    id: int = Field(..., description='bet id', json_schema_extra={'example': 1})
    status: str = Field(..., description='status',
                        json_schema_extra={'example': 'not_played'})
    created_at: datetime = Field(..., description='time created',
                                 json_schema_extra={'example': '2024-01-01T00:00:00'})
    updated_at: datetime = Field(..., description='time last updated',
                                 json_schema_extra={'example': '2024-01-01T00:00:00'})

    model_config = {"from_attributes": True}
