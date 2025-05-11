from pydantic import BaseModel

# Shared attributes for Service
class ServiceBase(BaseModel):
    name: str
    status: str

# Schema for creating a new Service
class ServiceCreate(ServiceBase):
    pass

# Schema for returning a Service
class Service(ServiceBase):
    id: int
    organization_id: int

    class Config:
        orm_mode = True

# Shared attributes for Incident
class IncidentBase(BaseModel):
    title: str
    description: str
    status: str

# Schema for creating a new Incident
class IncidentCreate(IncidentBase):
    pass

# Schema for returning an Incident
class Incident(IncidentBase):
    id: int
    service_id: int

    class Config:
        orm_mode = True
