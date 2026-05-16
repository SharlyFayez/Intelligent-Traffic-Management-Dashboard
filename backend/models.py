from sqlalchemy import Column, Integer, String
from database import Base

class TrafficData(Base):
    __tablename__ = "traffic_data"

    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)
    time = Column(String)
