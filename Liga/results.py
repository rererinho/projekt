from sqlmodel import Field, SQLModel, create_engine


class results(SQLModel, table=True):
    country: str
