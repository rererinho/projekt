import string

from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime

class LeaguesSeasonsFeed(SQLModel, table=True):
    id: int
    country: str
    name: str
    isCup: bool  #indicate if current tournament is cup or championship True – is cup tournament False – is championship tournament


