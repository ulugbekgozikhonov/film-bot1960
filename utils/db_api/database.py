# pip install sqlalchemy
# pip install psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(url="postgresql://postgres:root_123@localhost:5432/filmbotdb")
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)
