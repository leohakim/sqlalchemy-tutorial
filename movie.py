# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_ir', Integer, ForeignKey('actors.id'))
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


"""
The definition of this class and its mapping characteristics is quite simple. We start by making this class extend the Base class defined in the base.py module and then we add four properties to it:

A __tablename__ to indicate what is the name of the table that will support this class.
An id to represent the primary key in the table.
A title of type String.
A release_date of type Date.
"""
