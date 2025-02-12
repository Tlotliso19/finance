from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime

# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create engine with SSL settings
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require"
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="My Portfolio")
    created_at = Column(DateTime, default=datetime.utcnow)
    assets = relationship("Asset", back_populates="portfolio")

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    symbol = Column(String, index=True)
    value = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Store additional asset info
    name = Column(String)
    sector = Column(String)
    currency = Column(String)

    portfolio = relationship("Portfolio", back_populates="assets")

def init_db():
    """Initialize database with proper error handling"""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database initialization error: {str(e)}")
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()