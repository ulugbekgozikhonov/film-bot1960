from .database import Base
from sqlalchemy import Column,Integer,String



class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True,index=True)
    file_id = Column(String, nullable=False)
    caption = Column(String, nullable=False)
    code = Column(Integer, nullable=False,unique=True)
    
