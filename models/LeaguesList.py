import string

from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime

class LeaguesLists(SQLModel, table=True):
    id: int
    country: str
    name: str
    season: str
    date_start: datetime
    date_end: datetime
    isCup: bool #indicate if current tournament is cup or championship True – is cup tournament False – is championship tournament
    live_lineups: bool
    live_stats: bool
    path: str





