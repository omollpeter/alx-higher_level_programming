#!/usr/bin/python3
"""
This module contains class definition of a City

"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Defines a model for city linked to cities table

    Attributes:
        id (int): City id
        name (str): City name (max_length of 128 characters)
        state_id (int): states id in which the city belongs
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", back_populates="state")
