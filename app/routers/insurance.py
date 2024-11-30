from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import SessionLocal
from app.crud import get_tariff_by_date_and_type

router = APIRouter(prefix="/insurance", tags=["Insurance"])

@router.get("/calculate")
def calculate_insurance(cargo_type: str, declared_value: float, date: datetime, db: Session = Depends(SessionLocal)):
    tariff = get_tariff_by_date_and_type(db, cargo_type, date)
    if not tariff:
        return {"error": "No valid tariff found"}
    return {"insurance_cost": declared_value * tariff.rate}
