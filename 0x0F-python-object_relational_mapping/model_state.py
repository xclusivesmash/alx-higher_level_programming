#!/usr/bin/python3
"""
Module: model_state
Description: creates class for adding a table
on a specific database.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a base model from which to inherit
Base = declarative_base()


# Create a class model
class State(Base):
    """State class definition.
    Attributes:
        __tablename__ (str): name of the database table.
        id (int): primary key of the table.
        name (str): name of the state at hand.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
