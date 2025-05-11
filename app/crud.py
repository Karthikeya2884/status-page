from sqlalchemy.orm import Session
from app import models, schemas

def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def create_incident(db: Session, incident: schemas.IncidentCreate, service_id: int):
    db_incident = models.Incident(**incident.dict(), service_id=service_id)
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident