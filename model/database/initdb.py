from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
POSTGRES_URI = os.getenv("POSTGRES_URI")
engine = None
def connectInitDatabase():
    global engine
    try:
        engine = create_engine(POSTGRES_URI,echo=True)
        engine.connect();
        print("Database connected.")
        return engine
    except Exception as e :
        print(f"An error occurred: {e}")
        raise

def createSession():
    engine = connectInitDatabase();
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

connectInitDatabase();
dbSession = createSession();