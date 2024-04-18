import string

from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime
from LeaguesList import LeaguesLists

class Venue(SQLModel, table=True):
    id: int
    name: str