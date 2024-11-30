from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from app.kafka_logger import log_to_kafka
from datetime import datetime

router = APIRouter(prefix="/tariffs", tags=["Tariffs"])

@router.post("/")
def create_tariff(tariff: schemas.TariffCreate, db: Session = Depends(SessionLocal), user_id: int = None):
    new_tariff = crud.create_tariff(db, tariff)
    log_to_kafka(user_id, f"Created tariff {new_tariff.id}", datetime.now())
    return new_tariff

@router.delete("/{tariff_id}")
def delete_tariff(tariff_id: int, db: Session = Depends(SessionLocal), user_id: int = None):
    tariff = crud.get_tariff_by_date_and_type(db, tariff_id)
    if not tariff:
        raise HTTPException(status_code=404, detail="Tariff not found")
    crud.delete_tariff(db, tariff_id)
    log_to_kafka(user_id, f"Deleted tariff {tariff_id}", datetime.now())
    return {"detail": f"Tariff {tariff_id} deleted"}
