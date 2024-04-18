from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime
from LeaguesList import LeaguesLists

class LeagueTeamList(SQLModel, table=True):

    name: str
    country: str
    isCup: bool
    id: int | None = Field(default=None, foreign_key="LeaguesLists.id")