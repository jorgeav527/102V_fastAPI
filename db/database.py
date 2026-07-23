from sqlmodel import SQLModel, create_engine

from models.posts import Post  # noqa: F401
from models.users import User  # noqa: F401

engine = create_engine("sqlite:///database.db")

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    print("Tables created in database.db")
