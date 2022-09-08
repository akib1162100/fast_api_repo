from sqlalchemy import Column, Boolean, Integer, Float, String
from ..config import Base

class AgrimInfo(Base):
    __tablename__ = "agrim_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60))
    address = Column(String)
    balance = Column(Float(precision=4))