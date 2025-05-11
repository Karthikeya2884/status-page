from pydantic import BaseModel

class ServiceBase(BaseModel):
    name: str
    status: str

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    organization_id: int

    class Config:
        orm_mode = True

class IncidentCreate(BaseModel):
    title: str
    description: str
    status: str
