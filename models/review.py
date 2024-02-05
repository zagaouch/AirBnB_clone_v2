#!/usr/bin/python3
""" Review module for the HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        text = Column(String(1024), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    else:
        text = ""
        user_id = ""
        place_id = ""
