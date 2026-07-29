from sqlmodel import SQLModel, create_engine


# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
# connect_args = {"check_same_thread": False}
# engine = create_engine(sqlite_url, connect_args=connect_args)

# pip install python-dotenv
# from dotenv import load_dotenv
#
# # Load the variables from the .env file into the system environment
# load_dotenv()
#
# # Access the variables using os.getenv
# database_user = os.getenv("DB_USER")
# api_key = os.getenv("API_KEY")

database_url = "postgresql://user:password@db/dbname"
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
