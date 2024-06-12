from sqlmodel import Field
from sqlalchemy import Boolean

from .base import Base


class Houses(Base, table=True):
    __tablename__ = "houses"

    material: str
    pig_id: int | None = Field(default=None, foreign_key="pigs.id")
    successfully_attacked: bool = Field(sa_column=Boolean(), default=False)
