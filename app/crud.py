from datetime import datetime
from sqlalchemy.orm import Session
from app import models, schemas

def get_tariff_by_date_and_type(db: Session, cargo_type: str, date: datetime):
    return db.query(models.Tariff).filter(
        models.Tariff.cargo_type == cargo_type,
        models.Tariff.effective_date <= date
    ).order_by(models.Tariff.effective_date.desc()).first()

def create_tariff(db: Session, tariff: schemas.TariffCreate):
    db_tariff = models.Tariff(**tariff.dict())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff

def delete_tariff(db: Session, tariff_id: int):
    db.query(models.Tariff).filter(models.Tariff.id == tariff_id).delete()
    db.commit()
