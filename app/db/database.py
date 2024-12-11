from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = "sqlite:///./restaurant.db"

engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
