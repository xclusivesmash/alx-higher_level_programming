#!/usr/bin/python3
"""
Module: model_city
Description: creates class for adding a table
on a specific database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


# Create a class model
class City(Base):
    """State class definition.
    Attributes:
        __tablename__ (str): name of the database table.
        id (int): primary key of the table.
        name (str): name of the state at hand.
        state_id (int): foreign key to cities table.
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
