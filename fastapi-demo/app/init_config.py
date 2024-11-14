from sqlalchemy import create_engine
from .Utils.DAL.connector import PostSQLBase
from .Utils.DAL.Tables import Base

def startup_handler():
    PostSQLBase._engine = create_engine(
        "postgresql+pg8000://postgres:pass123@localhost/postgres"
    )
    Base.metadata.create_all(PostSQLBase._engine)
    

def shutdown_handler():
    pass
