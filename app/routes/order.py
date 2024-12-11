from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import create_order, get_orders, update_order
from app.db.database import SessionLocal
from app.utils.jwt_manager import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_order(order, db, user)

@router.get("/", response_model=list[OrderResponse])
def get_orders_endpoint(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_orders(db, user)

@router.put("/{order_id}", response_model=OrderResponse)
def update_order_endpoint(order_id: int, status: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return update_order(order_id, status, db, user)
