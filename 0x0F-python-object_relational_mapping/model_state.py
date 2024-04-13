#!/usr/bin/python3
"""
This module contains class definition of a state and an instance of
declarative_base()

"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Defines a model for state linked to states table

    Attributes:
        id (int): State id
        name (str): State name (max_length of 128 characters)
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(length=128), nullable=False)
