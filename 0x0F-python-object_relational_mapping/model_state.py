#!/usr/bin/python3
"""
Module containing the class definition of a State and Base instance.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# engine = create_engine(db_url)
Base = declarative_base()


class State(Base):
    """State class to implements states table in SQl db."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
