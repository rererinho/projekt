from sqlmodel import Field, SQLModel, create_engine

class tournament(SQLModel, table=True):
    league: str
    seanson: str
    id: int
