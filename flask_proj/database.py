import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
# Run in Flask-SQLAlchemy 3.1.x
class Box(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    comment: Mapped[str] = mapped_column(String)
    updated_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)


class Goods(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    comment: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    updated_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    created_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    box_id: Mapped[int] = mapped_column(ForeignKey("box.id"))

#
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
#
# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['DATABASE'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = dict_factory  # Returns query results as a dictionary
#     return g.db
#
#
# def close_db(e=None):
#     db = g.pop('db', None)
#
#     if db is not None:
#         db.close()
#
#
# def init_db():
#     db = SQLAlchemy(model_class=Base)
#
#     class User(db.Model):
#         id: Mapped[int] = mapped_column(Integer, primary_key=True)
#         username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
#         email: Mapped[str] = mapped_column(String)
#
#     # db = get_db()
#     db.create_all()
#
#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))
#
#
# @click.command('init-db')
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')
#
#
# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)
