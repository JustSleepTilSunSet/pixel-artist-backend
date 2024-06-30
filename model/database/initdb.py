from sqlalchemy import create_engine
import os
POSTGRES_URI = os.getenv("POSTGRES_URI")
def connectInitDatabase():
    try:
        engine = create_engine(POSTGRES_URI,echo=True)
        engine.connect();
        print("Database connected.")
        return engine
    except Exception as e :
        print(f"An error occurred: {e}")
        raise