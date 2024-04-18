from sqlmodel import Field, SQLModel, create_engine

class match(SQLModel, table=True):
    date: str
    time: str
    status: str
    venue: str
    venue_id: int
    venue_city: str
    static_id: int