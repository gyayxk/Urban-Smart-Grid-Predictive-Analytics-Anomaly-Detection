from sqlalchemy import create_engine, Column, Float, DateTime, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///smart_grid_analytics.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class EnergyRecord(Base):
    __tablename__ = "energy_consumption"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, unique=True)
    consumption = Column(Float)
    temperature = Column(Float)
    is_holiday = Column(Boolean, default=False)
    anomaly_flag = Column(Integer, default=0)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Database Initialized!")