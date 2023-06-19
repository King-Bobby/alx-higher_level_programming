#!/usr/bin/python3
"""
Module that defines the City class
"""


from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class that represents a city in the database
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
