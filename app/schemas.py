from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    status: str
class IncidentCreate(BaseModel):
    title: str
    description: str
    status: str
