from sqlmodel import Field
from sqlalchemy import Boolean

from .base import Base


class Attacks(Base, table=True):
    __tablename__ = "attacks"

    wolf_id: int | None = Field(default=None, foreign_key="wolves.id")
    house_id: int | None = Field(default=None, foreign_key="houses.id")
    success:  bool = Field(sa_column=Boolean(), default=False)
    # SQLModel doesn't like booleans, but SQLAlchemy does
