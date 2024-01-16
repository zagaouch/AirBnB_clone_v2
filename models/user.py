#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    email = Column(128, nullable=False)
    password = Column(128, nullable=False)
    first_name = Column(128, nullable=False)
    last_name = Column(128, nullable=False)
    places = relationship("Place", backref="user", case="delete")
    reviews = relationship("Review", backref="user", case="delete")
