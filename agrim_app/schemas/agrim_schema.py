from pydantic import BaseModel

# class CompanyBase(BaseModel):

class AgrimCreate(BaseModel):
    name: str
    address: str
    balance: float
    
class AgrimItem(AgrimCreate):
    id: int

    class Config:
        orm_mode = True