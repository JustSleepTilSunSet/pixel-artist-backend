
from sqlalchemy import create_engine
import os
POSTGRES_URI = os.getenv("POSTGRES_URI")
engine = create_engine(POSTGRES_URI,echo=True)
engine.connect();
print("Database connected.")