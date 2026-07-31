import os

from sqlmodel import SQLModel, create_engine

from dotenv import load_dotenv

# Load the variables from the .env file into the system environment
load_dotenv()

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)

database_url = os.getenv("DB_URL", "")
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
