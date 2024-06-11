from sqlmodel import Field

from .base import Base


class Houses(Base, table=True):
    __tablename__ = "houses"

    material: str
    pig_id: int | None = Field(default=None, foreign_key="pigs.id")
