from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.order import Order, OrderStatus
from datetime import datetime
import json

def create_order(order_data, db: Session, user):
    new_order = Order(customer_id=user.id, items=json.dumps(order_data.items))
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session, user):
    if user.role == "customer":
        return db.query(Order).filter(Order.customer_id == user.id).all()
    return db.query(Order).all()

def update_order(order_id, status, db: Session, user):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if user.role == "customer" and order.customer_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this order")
    if user.role == "customer" and order.status != OrderStatus.PENDING:
        raise HTTPException(status_code=400, detail="Cannot modify this order")
    order.status = OrderStatus[status.upper()]
    order.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(order)
    return order
