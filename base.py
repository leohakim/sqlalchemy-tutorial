# coding=utf-8

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# string_connection = 'postgresql://user:admin@0.0.0.0:5432/sqlalchemy'

engine = create_engine(string_connection)

Session = sessionmaker(bind=engine)


Base = declarative_base()

"""
This code creates:

a SQLAlchemy Engine that will interact with our dockerized PostgreSQL database,
a SQLAlchemy ORM session factory bound to this engine,
and a base class for our classes definitions.
"""

