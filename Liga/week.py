from sqlmodel import Field, SQLModel, create_engine

class week(SQLModel, table=True):
    number: int
