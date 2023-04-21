from datetime import datetime
from typing import List

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str
    

class Operation(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: datetime
    type: str
    

    class Config:
        orm_mode = True
        

class OperationResponse(BaseModel):
    status: str
    data: List[Operation]
    details: str = None