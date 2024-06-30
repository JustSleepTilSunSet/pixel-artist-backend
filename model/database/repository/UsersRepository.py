from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model.database.repository.UserField import account,password
import os
POSTGRES_URI = os.getenv("POSTGRES_URI")
TABLE_NAME_USER = os.getenv("TABLE_NAME_USER")
Base = declarative_base()

class User(Base):
    __tablename__ = TABLE_NAME_USER
    account = account
    password = password
