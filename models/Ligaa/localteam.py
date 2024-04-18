from sqlmodel import Field, SQLModel, create_engine

class localteam(SQLModel, table=True):
    name: str
    score: int
    ft_score: int
    et_score: int
    pen_score: int
    id: int
