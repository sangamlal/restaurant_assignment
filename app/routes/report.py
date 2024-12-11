from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.report_service import generate_sales_report
from app.db.database import SessionLocal
from app.utils.jwt_manager import get_current_admin

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sales")
def sales_report(start_date: str, end_date: str, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return generate_sales_report(start_date, end_date, db)
