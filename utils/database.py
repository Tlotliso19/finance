from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime

# Get database URL from environment
DATABASE_URL = 'postgresql://postgres:BSwtGv4AvaKvoYJD@quarterly-prominent-seagull.data-1.use1.tembo.io:5432/postgres'
##os.getenv('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create engine with proper SSL and connection pooling settings
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require",
        "connect_timeout": 30
    },
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
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
    """Get database session with proper error handling"""
    db = None
    try:
        db = SessionLocal()
        return db
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        if db:
            db.close()
        raise