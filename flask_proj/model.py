import datetime

from database import db
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
class Box(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    comment: Mapped[str] = mapped_column(String)
    updated_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_time: Mapped[datetime.datetime] = mapped_column(DateTime)


class Goods(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    comment: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    updated_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    box_id: Mapped[int] = mapped_column(ForeignKey("Box.id"))
