from sqlmodel import Field, SQLModel, create_engine

class vistorteam(SQLModel, table=True):
    name: str
    score: int
    ft_score: int
    et_score: int
    pen_score: int
    id: int
