# Define Models

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False, default='todo')
    createdAt = Column(DateTime, nullable=False, default=datetime.now)
    updatedAt = Column(DateTime, nullable=False,default=datetime.now, onupdate=datetime.now)
    