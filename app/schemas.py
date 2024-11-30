from pydantic import BaseModel
from datetime import datetime

class TariffBase(BaseModel):
    cargo_type: str
    rate: float
    effective_date: datetime

class TariffCreate(TariffBase):
    pass

class Tariff(TariffBase):
    id: int

    class Config:
        orm_mode = True

class LogCreate(BaseModel):
    user_id: int = None
    action: str
    timestamp: datetime
