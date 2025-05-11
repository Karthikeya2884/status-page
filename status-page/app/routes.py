from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/services/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    return crud.create_service(db, service)

@router.post("/services/{service_id}/incidents/", response_model=schemas.Incident)
def create_incident(service_id: int, incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    return crud.create_incident(db, incident, service_id)