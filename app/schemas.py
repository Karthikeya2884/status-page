from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    status: str
