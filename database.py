from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.exc import SQLAlchemyError
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    try:
        SQLModel.metadata.create_all(engine)
    except SQLAlchemyError as e:
        print("Error creating DB:", e)

def get_session():
    with Session(engine) as session:
        yield session
