from fastapi import FastAPI
from app.routes import auth, order, report
from app.db.database import engine
from app.models import Base

# Initialize app and create tables
app = FastAPI(title="Restaurant Order API", version="1.0.0")

Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
app.include_router(report.router, prefix="/report", tags=["Reports"])
