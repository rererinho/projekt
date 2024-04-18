from sqlmodel import Field, SQLModel, create_engine

class stage(SQLModel, table=True):
    name:str
    round:str
    gid:int
    is_current: bool
    stage_id: int