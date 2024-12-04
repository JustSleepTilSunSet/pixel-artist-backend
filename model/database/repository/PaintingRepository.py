from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model.database.repository.PaintingField import account,paintingName, paintingDescription, customName
import os
POSTGRES_URI = os.getenv("POSTGRES_URI")
TABLE_NAME_PAINTING = os.getenv("TABLE_NAME_PAINTING")
Base = declarative_base()

class Painting(Base):
    __tablename__ = TABLE_NAME_PAINTING
    account = account
    paintingName = paintingName
    paintingDescription = paintingDescription
    customName = customName
    def to_dict(self):
       return {
           "customName": self.customName,
           "paintingDescription": self.paintingDescription,
       }