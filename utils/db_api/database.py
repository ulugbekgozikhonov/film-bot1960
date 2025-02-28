# pip install sqlalchemy
# pip install psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine(url="postgresql://postgres:wMNkkRawSXIiwfcjHfaWExwXoqNERLAr@shinkansen.proxy.rlwy.net:35751/railway")
LocalSession = sessionmaker(bind=engine,autoflush=False,autocommit=False)

