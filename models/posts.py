from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from models.users import User


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    autor: int = Field(foreign_key="user.id")
    contenido: str
    titulo: str
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )

    user: User = Relationship()
