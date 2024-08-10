from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('POSTGRES_HOST')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DATABASE')

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()