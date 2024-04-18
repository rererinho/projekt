from sqlmodel import Field, SQLModel, create_engine

class Tournament(SQLModel, table=True):
    id: int
    league: str
    season: str
