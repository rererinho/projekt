from sqlmodel import Field, SQLModel, create_engine

class Stage(SQLModel, table=True):
    stage_id: int
    g_id: int
    name: str
    round: str
    is_current: bool


