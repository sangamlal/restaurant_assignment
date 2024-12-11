from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItem(BaseModel):
    name: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
