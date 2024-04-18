from sqlmodel import Field, SQLModel, create_engine

class aggregate(SQLModel, table=True):
    first_team:str
    second_team:str
    winner:int
    score:str
