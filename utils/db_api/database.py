# pip install sqlalchemy
# pip install psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(url="sqlite:///./filbot.db")
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)
