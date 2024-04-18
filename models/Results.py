
from sqlmodel import Field, SQLModel, create_engine

class Results(SQLModel, table=True):
    country: str